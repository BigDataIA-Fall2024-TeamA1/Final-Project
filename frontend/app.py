import streamlit as st
import requests

# API URL
API_URL_TEXT = "http://127.0.0.1:8000/generate_summary"
API_URL_FILE = "http://127.0.0.1:8000/upload_file_summary"

st.title("Legal Case Summary Generator")

# 选项：用户选择输入还是上传文件
option = st.radio("Choose Input Method:", ["Enter Details Manually", "Upload a File"])

if option == "Enter Details Manually":
    st.header("Input Details to Generate Summary")
    facts = st.text_area("Enter Facts", placeholder="Provide the facts of the case.")
    issues = st.text_area("Enter Issues", placeholder="What are the key issues of the case?")
    reasoning = st.text_area("Enter Reasoning", placeholder="Provide the reasoning or legal arguments.")
    decision = st.text_area("Enter Decision", placeholder="What was the decision or outcome?")

    if st.button("Generate Summary"):
        # 构造请求体
        request_data = {
            "facts": facts,
            "issues": issues,
            "reasoning": reasoning,
            "decision": decision
        }
        try:
            response = requests.post(API_URL_TEXT, json=request_data)
            if response.status_code == 200:
                data = response.json()
                st.subheader("Generated Summary")
                st.write(data["summary"])
            else:
                st.error(f"Error: {response.status_code}")
                st.error(response.json().get("detail", "Unknown error"))
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

elif option == "Upload a File":
    st.header("Upload a File to Generate Summary")
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])

    if st.button("Generate Summary from File") and uploaded_file:
        try:
            files = {"file": (uploaded_file.name, uploaded_file.read(), "application/octet-stream")}
            response = requests.post(API_URL_FILE, files=files)
            if response.status_code == 200:
                data = response.json()
                st.subheader("Generated Summary")
                st.write(data["summary"])
            else:
                st.error(f"Error: {response.status_code}")
                st.error(response.json().get("detail", "Unknown error"))
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")