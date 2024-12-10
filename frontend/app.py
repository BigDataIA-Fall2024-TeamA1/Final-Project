import streamlit as st
import requests

# Backend API URL
BASE_URL = "http://127.0.0.1:8000"

# Streamlit Page Configuration
st.set_page_config(
    page_title="Legal Assistant Chat",
    page_icon="⚖️",
    layout="wide",
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! I'm your Legal Assistant. How can I help you today?"}
    ]
if "current_task" not in st.session_state:
    st.session_state["current_task"] = None

# Sidebar: Saved Chats
with st.sidebar:
    st.title("Saved Chats")
    saved_chats = st.radio("Select a chat", ["New Chat"] + ["Chat 1", "Chat 2"])
    if st.button("Start New Chat"):
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hello! I'm your Legal Assistant. How can I help you today?"}
        ]
        st.session_state["current_task"] = None

# Chat Display
st.title("💼 Legal Case Assistant")
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Welcome Message and Task Buttons
if not st.session_state["current_task"]:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Summarize Document"):
            st.session_state["current_task"] = "summarize"
            st.session_state["messages"].append(
                {"role": "assistant", "content": "Would you like to summarize an existing case or upload a document?"}
            )
    with col2:
        if st.button("Generate Report"):
            st.session_state["current_task"] = "report"
            st.session_state["messages"].append(
                {"role": "assistant", "content": "Let's generate a report. Please provide the required information."}
            )
    with col3:
        if st.button("Generate Strategy"):
            st.session_state["current_task"] = "strategy"
            st.session_state["messages"].append(
                {"role": "assistant", "content": "Would you like to use an existing case or provide details?"}
            )

# Interactive Chat Area
if st.session_state["current_task"]:
    user_input = st.chat_input("Type your response here...")
    uploaded_file = st.file_uploader("Upload a document (optional)", type=["txt", "pdf", "docx"])

    # Handle User Input
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        task = st.session_state["current_task"]

        if task == "summarize":
            if "existing" in user_input.lower():
                case_id = st.text_input("Enter Case ID (Docket Number):")
                if st.button("Fetch Summary") and case_id:
                    response = requests.post(f"{BASE_URL}/summarize", json={"case_id": case_id})
                    if response.status_code == 200:
                        summary = response.json().get("response", "No summary available.")
                        st.session_state["messages"].append({"role": "assistant", "content": summary})
                        st.chat_message("assistant").write(summary)
                    else:
                        st.error("Error fetching case summary. Please check the case ID.")
            elif uploaded_file:
                file_content = uploaded_file.read().decode("utf-8")
                response = requests.post(f"{BASE_URL}/summarize", json={"content": file_content})
                if response.status_code == 200:
                    summary = response.json().get("response", "No summary available.")
                    st.session_state["messages"].append({"role": "assistant", "content": summary})
                    st.chat_message("assistant").write(summary)
                else:
                    st.error("Error summarizing the document.")
            else:
                st.error("Please provide a case ID or upload a document to summarize.")

        elif task == "report":
            # Collect Report Metadata
            metadata = {
                "lawyer_name": st.text_input("Lawyer Name"),
                "law_firm": st.text_input("Law Firm"),
                "court": st.text_input("Court"),
                "jurisdiction": st.text_input("Jurisdiction"),
                "facts": st.text_area("Facts"),
                "issues": st.text_area("Issues"),
                "reasoning": st.text_area("Reasoning"),
                "decision": st.text_area("Decision"),
            }
            if st.button("Generate Report"):
                if all(metadata.values()):
                    response = requests.post(f"{BASE_URL}/generate_report", json=metadata)
                    if response.status_code == 200:
                        report = response.json().get("response", "No report generated.")
                        st.session_state["messages"].append({"role": "assistant", "content": report})
                        st.chat_message("assistant").write(report)
                    else:
                        st.error("Error generating report.")
                else:
                    st.error("Please fill in all the fields before generating the report.")

        elif task == "strategy":
            # Collect Strategy Details
            strategy_details = {
                "facts": st.text_area("Facts"),
                "issues": st.text_area("Issues"),
                "reasoning": st.text_area("Reasoning"),
                "decision": st.text_area("Decision"),
            }
            if st.button("Generate Strategy"):
                if all(strategy_details.values()):
                    response = requests.post(f"{BASE_URL}/generate_strategy", json=strategy_details)
                    if response.status_code == 200:
                        strategy = response.json().get("response", "No strategy generated.")
                        st.session_state["messages"].append({"role": "assistant", "content": strategy})
                        st.chat_message("assistant").write(strategy)
                    else:
                        st.error("Error generating strategy.")
                else:
                    st.error("Please provide all required details to generate a strategy.")

        # Reset Current Task
        if st.button("Reset Task"):
            st.session_state["current_task"] = None
