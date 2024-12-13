import streamlit as st
import requests

# Adjust the URL to the location of your FastAPI backend
API_URL = "http://localhost:8000"

st.title("Legal Case Summary Generator")

option = st.radio("Choose input method", ("Upload a file", "Input details manually"))

if option == "Upload a file":
    uploaded_file = st.file_uploader("Please upload the case file (txt, pdf, docx, jpg, png)")
    if uploaded_file is not None:
        # Send file to backend
        files = {'file': (uploaded_file.name, uploaded_file.read(), uploaded_file.type)}
        response = requests.post(f"{API_URL}/upload_file", files=files)  # Adjusted API endpoint for file upload
        
        if response.status_code == 200:
            data = response.json()
            if data.get("report"):
                st.subheader("Generated Summary")
                # Display summary in a scrollable text area
                st.text_area("Summary", data["report"], height=300)
            else:
                st.write(data.get("message", "No summary generated."))
        else:
            st.error("Error processing file. Check the backend logs.")
            
elif option == "Input details manually":
    # Collect user input
    facts = st.text_area("Enter Facts")
    issues = st.text_area("Enter Issues")
    reasoning = st.text_area("Enter Reasoning")
    decision = st.text_area("Enter Decision")

    if st.button("Generate Summary"):
        # Construct request data
        request_data = {
            "facts": facts,
            "issues": issues,
            "reasoning": reasoning,
            "decision": decision
        }
        
        # Send request to backend
        response = requests.post(f"{API_URL}/generate_summary", json=request_data)  # Adjusted API endpoint for summary generation
        
        if response.status_code == 200:
            data = response.json()
            if data.get("summary"):
                st.subheader("Generated Summary")
                # Display summary in a scrollable text area
                st.text_area("Summary", data["summary"], height=300)
            else:
                st.write(data.get("message", "No summary generated."))
        else:
            st.error("Error processing input. Check the backend logs.")
