import os
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "legal-case-index")  # Default index name

# Initialize Pinecone
pc = Pinecone(
    api_key=PINECONE_API_KEY
)

# Connect to the index
index = pc.Index(INDEX_NAME)

# Query by docket number
docket_number_to_query = "COA23-1057"

print(f"Querying for docket number: {docket_number_to_query}...")
response = index.query(
    vector=[0.0] * 1536,  # Dummy vector; the filter takes precedence here
    top_k=10,  # Number of top results to return
    include_metadata=True,  # Include metadata in the response
    filter={
        "docket_number": {"$eq": docket_number_to_query}  # Filter by exact match on docket_number
    }
)

print("Query Results:", response)
