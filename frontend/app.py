import streamlit as st
import requests

# Backend Base URL
BACKEND_URL = "http://127.0.0.1:8000"

# Sidebar for Agent Selection
st.sidebar.title("Legal Case Assistant")
agent = st.sidebar.radio(
    "Choose an Agent",
    [
        "Generate Report",
        "Search Legal Resources",
        "Retrieve Relevant Cases",
        "Generate Strategy"
    ]
)

# Right Pane - Dynamic Content
if agent == "Generate Report":
    st.title("Generate Legal Report")

    # User inputs for metadata
    lawyer_name = st.text_input("Lawyer Name", key="lawyer_name")
    law_firm = st.text_input("Law Firm Name", key="law_firm")
    court = st.text_input("Court Name", key="court_name")
    jurisdiction = st.text_input("Jurisdiction", key="jurisdiction")
    facts = st.text_area("Facts", key="facts")
    issues = st.text_area("Issues", key="issues")
    reasoning = st.text_area("Reasoning", key="reasoning")
    decision = st.text_area("Decision", key="decision")
    feedback = st.text_area("Feedback for Improvement (Optional)", key="feedback")

    if st.button("Generate Report"):
        if all([lawyer_name, law_firm, court, jurisdiction, facts, issues, reasoning, decision]):
            with st.spinner("Generating report..."):
                metadata = {
                    "lawyer_name": lawyer_name,
                    "law_firm": law_firm,
                    "court": court,
                    "jurisdiction": jurisdiction,
                    "facts": facts,
                    "issues": issues,
                    "reasoning": reasoning,
                    "decision": decision,
                    "feedback": feedback
                }
                response = requests.post(f"{BACKEND_URL}/solution2/report", json=metadata)

                if response.status_code == 200:
                    result = response.json()
                    report_content = result["report_content"]
                    word_file = result["word_file"]
                    pdf_file = result["pdf_file"]

                    st.subheader("Generated Report")
                    st.write(report_content)

                    st.download_button("Download as Word", word_file, file_name="legal_report.docx")
                    st.download_button("Download as PDF", pdf_file, file_name="legal_report.pdf")

                    if st.button("Regenerate Report"):
                        st.write("Provide feedback in the 'Feedback' section and click 'Generate Report' again.")
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        else:
            st.error("Please fill in all required fields!")

elif agent == "Search Legal Resources":
    st.title("Search Legal Resources")
    query = st.text_input("Enter Search Query", key="search_query")

    if st.button("Search", key="search_button"):
        if query.strip():
            with st.spinner("Searching..."):
                response = requests.post(f"{BACKEND_URL}/solution2/search", json={"query": query})

                if response.status_code == 200:
                    results = response.json().get("results", [])
                    st.subheader("Search Results:")
                    for result in results:
                        st.write(f"- [{result['title']}]({result['link']})")
                        st.write(result['snippet'])
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        else:
            st.error("Please enter a search query!")

elif agent == "Retrieve Relevant Cases":
    st.title("Retrieve Relevant Court Cases")
    case_query = st.text_input("Enter Case Query", key="case_query")

    if st.button("Retrieve Cases", key="retrieve_cases"):
        if case_query.strip():
            with st.spinner("Retrieving cases..."):
                response = requests.post(f"{BACKEND_URL}/solution2/cases", json={"query": case_query})

                if response.status_code == 200:
                    cases = response.json().get("cases", [])
                    st.subheader("Relevant Cases:")
                    for case in cases:
                        st.write(f"- [{case['title']}]({case['url']})")
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        else:
            st.error("Please enter a case query!")

elif agent == "Generate Strategy":
    st.title("Generate Legal Strategy")

    # User inputs for metadata
    facts = st.text_area("Facts", key="strategy_facts")
    issues = st.text_area("Issues", key="strategy_issues")
    reasoning = st.text_area("Reasoning", key="strategy_reasoning")
    decision = st.text_area("Decision", key="strategy_decision")

    if st.button("Generate Strategy", key="generate_strategy"):
        if all([facts, issues, reasoning, decision]):
            with st.spinner("Generating strategy..."):
                metadata = {
                    "facts": facts,
                    "issues": issues,
                    "reasoning": reasoning,
                    "decision": decision
                }
                response = requests.post(f"{BACKEND_URL}/solution2/strategy", json={"metadata": metadata})

                if response.status_code == 200:
                    strategy = response.json().get("strategy", "No strategy available.")
                    st.subheader("Generated Strategy:")
                    st.write(strategy)
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        else:
            st.error("Please fill in all required fields!")
