from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import Optional
from langchain.agents import tool, initialize_agent, Tool, ZeroShotAgent
from langchain.vectorstores import Pinecone as LangPinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RouterChain
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
import os
import requests

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# Initialize OpenAI LLM
llm = ChatOpenAI(model="gpt-4", openai_api_key=OPENAI_API_KEY, temperature=0.7)

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
if PINECONE_INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
pinecone_index = pc.Index(PINECONE_INDEX_NAME)
vector_store = LangPinecone(
    index=pinecone_index,
    embedding_function=OpenAIEmbeddings(),
    text_key="text",
)

# FastAPI App
app = FastAPI()

# Define Data Models
class Metadata(BaseModel):
    lawyer_name: str
    law_firm: str
    court: str
    jurisdiction: str
    facts: str
    issues: str
    reasoning: str
    decision: str

class UserQuery(BaseModel):
    query: str

class SummarizeRequest(BaseModel):
    case_id: Optional[str] = None
    content: Optional[str] = None

class StrategyRequest(BaseModel):
    facts: str
    issues: str
    reasoning: str
    decision: str

# Tool: Summarization Agent
@tool("summarize", return_direct=True)
def summarize_tool(case_id: Optional[str] = None, content: Optional[str] = None):
    """
    Summarize a legal case or document.

    Args:
        case_id (Optional[str]): The case ID (docket number) to summarize.
        content (Optional[str]): The content of the document to summarize.

    Returns:
        str: A summary of the case or document.
    """
    if case_id:
        # Use Pinecone to fetch the document with the matching docket number
        results = pinecone_index.query(
            vector=None,  # No vector required for metadata search
            filter={"docket_number": case_id},  # Match on docket_number metadata
            top_k=1,
            include_metadata=True
        )
        if not results["matches"]:
            return f"No document found for docket number: {case_id}."
        doc_content = results["matches"][0]["metadata"]["text"]
        prompt = f"Summarize this legal case:\n\n{doc_content}"
        response = llm([{"role": "user", "content": prompt}])
        return response.content
    elif content:
        # Summarize the provided content
        prompt = f"Summarize this legal document:\n\n{content}"
        response = llm([{"role": "user", "content": prompt}])
        return response.content
    else:
        return "Error: Please provide either a case ID (docket number) or document content."

# Tool: Report Generation Agent
@tool("generate_report", return_direct=True)
def generate_report_tool(metadata: Metadata):
    """
    Generate a detailed legal report based on provided metadata.

    Args:
        metadata (Metadata): The metadata containing details for the report.

    Returns:
        str: A structured legal report.
    """
    prompt = f"""
    Lawyer: {metadata.lawyer_name}
    Law Firm: {metadata.law_firm}
    Court: {metadata.court}
    Jurisdiction: {metadata.jurisdiction}
    Facts: {metadata.facts}
    Issues: {metadata.issues}
    Reasoning: {metadata.reasoning}
    Decision: {metadata.decision}
    
    Structure the report as follows:
    1. Introduction
    2. Statement of Facts
    3. Discussion
    4. Conclusion
    """
    response = llm([HumanMessage(content=prompt)])
    return response.content

# Tool: Strategy Generation Agent
@tool("generate_strategy", return_direct=True)
def generate_strategy_tool(facts: str, issues: str, reasoning: str, decision: str):
    """
    Generate a comprehensive legal strategy based on case details.

    Args:
        facts (str): The facts of the case.
        issues (str): The legal issues involved.
        reasoning (str): The legal reasoning applied.
        decision (str): The decision or outcome of the case.

    Returns:
        str: A detailed legal strategy.
    """
    prompt = f"""
    Facts: {facts}
    Issues: {issues}
    Reasoning: {reasoning}
    Decision: {decision}
    
    Provide a comprehensive legal strategy that includes:
    - Recommended legal actions
    - Potential alternative approaches
    - Counterarguments and responses
    - Suggestions on trial, settlement, or other actions
    """
    response = llm([HumanMessage(content=prompt)])
    return response.content

# Tool: Web Search Agent
@tool("web_search", return_direct=True)
def web_search_tool(query: str):
    """
    Perform a web search for legal resources.

    Args:
        query (str): The search query.

    Returns:
        list: A list of search results.
    """
    serpapi_url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
    }
    response = requests.get(serpapi_url, params=params)
    if response.status_code != 200:
        return "Failed to fetch web search results."
    return response.json().get("organic_results", [])

# Tool: Case Retrieval Agent
@tool("retrieve_case", return_direct=True)
def retrieve_case_tool(query: str):
    """
    Retrieve relevant court cases based on a query.

    Args:
        query (str): The query to search for relevant cases.

    Returns:
        str: A list of relevant cases.
    """
    docs = vector_store.similarity_search(query, k=5)
    if not docs:
        return "No relevant cases found."
    results = []
    for doc in docs:
        metadata = doc.metadata
        results.append(f"Case: {metadata.get('docket_number')}, Summary: {doc.page_content[:200]}...")
    return "\n".join(results)

# Task Routing Prompt
router_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
    Classify the user query into one of the following tasks:
    1. summarize
    2. generate_report
    3. generate_strategy
    4. web_search
    5. retrieve_case

    Query: {query}
    Task:
    """,
)



# Define Tools
tools = [
    Tool(name="Summarize Tool", func=summarize_tool, description="Summarize legal cases or documents."),
    Tool(name="Generate Report Tool", func=generate_report_tool, description="Generate a legal report."),
    Tool(name="Generate Strategy Tool", func=generate_strategy_tool, description="Generate a legal strategy."),
    Tool(name="Web Search Tool", func=web_search_tool, description="Perform a web search for legal resources."),
    Tool(name="Retrieve Case Tool", func=retrieve_case_tool, description="Retrieve relevant court cases."),
]

# Initialize Agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Endpoints

@app.post("/summarize")
async def summarize_endpoint(request: SummarizeRequest):
    """Summarize an existing case or uploaded content."""
    try:
        if request.case_id:
            result = summarize_tool(case_id=request.case_id)
        elif request.content:
            result = summarize_tool(content=request.content)
        else:
            raise HTTPException(status_code=400, detail="Provide a case_id or content to summarize.")
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate_report")
async def generate_report_endpoint(metadata: Metadata):
    """Generate a detailed legal report."""
    try:
        report_content = generate_report_tool(metadata)
        return {"response": report_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_strategy")
async def generate_strategy_endpoint(request: StrategyRequest):
    """Generate a comprehensive legal strategy."""
    try:
        strategy_content = generate_strategy_tool(
            facts=request.facts,
            issues=request.issues,
            reasoning=request.reasoning,
            decision=request.decision,
        )
        return {"response": strategy_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/web_search")
async def web_search_endpoint(query: UserQuery):
    """Perform a web search for legal resources."""
    try:
        results = web_search_tool(query.query)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/retrieve_case")
async def retrieve_case_endpoint(query: UserQuery):
    """Retrieve relevant court cases."""
    try:
        results = retrieve_case_tool(query.query)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat_endpoint(query: UserQuery):
    """Route query to the appropriate agent."""
    try:
        # Use the agent to handle the query dynamically
        response = agent.run(input=query.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

