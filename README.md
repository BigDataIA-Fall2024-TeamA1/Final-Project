# Final Project 

---

## Attestation and Contribution Declaration

WE ATTEST THAT WE HAVEN'T USED ANY OTHER STUDENTS' WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK.

**Contribution Breakdown**:
- Chiu Meng Che: 34%  
- Shraddha Bhandarkar: 33%  
- Kefan Zhang: 33%  

---

## Workflow Diagram

![workflow](images/workflow_diagram.jpeg)

---
## Project Overview

### 1. Introduction  

**Background**:  
This project addresses inefficiencies in legal document management and analysis by leveraging modern data processing pipelines and machine learning models, including large language models (LLMs), to enhance fraud detection, dispute categorization, and decision-making.  

**Objective**:  
Develop an end-to-end system that automates data ingestion, preprocessing, and legal document analysis, enabling users to interact with results through an intuitive application.  

---

### 2. Scope  

**Boundaries**:  
- **Data Sources**: CourtListener API for legal documents.  
- **Technologies**: Apache Airflow, FastAPI, Streamlit, Pinecone, OpenAI GPT-4, and Snowflake.  
- **Deliverables**: A fully functional application with a backend API, ETL pipeline, LLM integration, and an interactive front-end interface.

**Stakeholders**:  
- Legal professionals seeking insights from past cases.  
- Organizations aiming to enhance fraud detection and dispute resolution processes.

---

### 3. Problem Statement  

**Current Challenges**:  
- Manual analysis of legal documents is time-intensive and prone to errors.  
- Limited tools for automated fraud detection, dispute categorization, and detailed summaries.  

**Opportunities**:  
- Streamlined legal analysis using AI-powered automation, including advanced LLM capabilities.  
- Improved decision-making with detailed case summaries, similarity searches, and actionable recommendations.  

---

### 4. Methodology  

**Data Sources**:  
- CourtListener API or scraped legal documents.  

**Technologies and Tools**:  
- **ETL**: Apache Airflow.  
- **Backend**: FastAPI for API management.  
- **Frontend**: Streamlit for user interaction.  
- **Data Storage**: Snowflake for structured data and Pinecone for vector embeddings.  
- **Models**:  
  - **OpenAI GPT-4**: Used for generating case summaries, detecting potential fraud, categorizing disputes, and providing recommendations.  
  - **HuggingFace Embeddings**: e.g., `all-MiniLM-L6-v2` for converting legal texts into vector embeddings for similarity searches.  
  - **Custom Fraud Detection Classifiers**: Built using scikit-learn or PyTorch.  

**Data Pipeline Design**:  
1. **Ingestion**: Automate fetching and storing raw data.  
2. **Preprocessing**: Clean text, extract metadata, generate embeddings, and add fraud labels.  
3. **Storage**: Store raw and processed data in appropriate databases.  

**LLM Integration**:  
- **Fraud Detection**: Use LLMs to analyze case descriptions for fraud indicators with prompts like:  
  `"Does this text suggest potential fraud? Provide reasoning."`  
- **Dispute Categorization**: Employ LLMs to classify disputes into predefined categories such as liability disputes or coverage disputes.  
- **Summarization**: Generate concise case summaries using LLMs with prompts such as:  
  `"Summarize this legal case in less than 200 words, focusing on the main legal issues and outcome."`  
- **Recommendation Engine**: Suggest next steps by analyzing similar cases with LLMs.  

**Data Processing and Transformation**:  
- Use Python-based EDA to explore data and ensure quality transformations.  
- Leverage LLM-generated embeddings for similarity searches and contextual analysis.  

---

### 5. Project Plan and Timeline  

**Milestones and Deliverables**:  
1. **Day 1-3**: Data ingestion pipeline setup with Apache Airflow.  
2. **Day 3-5**: Preprocessing scripts for text cleaning and embedding generation.  
3. **Day 5-7**: Pinecone integration for similarity search.  
4. **Day 7-12**: LLM integration for fraud detection, categorization, and summaries.  
5. **Day 1-18**: Backend API development with FastAPI.  
6. **Day 1-18**: Frontend dashboard implementation with Streamlit.  
7. **Day 18-22**: Testing and deployment on a cloud platform.  

---

### 6. Resources and Team  

**Personnel**:  
- **Member 1**: Pipeline and model implementation, including LLM integration.  
- **Member 2**: Backend development and API integration.  
- **Member 3**: Frontend development and user interface design.  

---

### 7. Risks and Mitigation Strategies  

**Potential Risks**:  
1. Inconsistent or missing data from external APIs.  
2. Integration challenges between components (ETL, backend, frontend, LLM).  

**Mitigation Strategies**:  
- Perform data quality checks during ingestion.  
- Use containerization (Docker) to ensure seamless integration.  
- Apply LLM prompt engineering techniques to enhance performance.  

---

### 8. Expected Outcomes and Benefits  

**Measurable Goals**:  
- Automate ingestion and preprocessing for at least 90% of incoming legal documents.  
- Achieve over 80% accuracy in fraud detection and dispute categorization.  
- Provide clear, actionable summaries for 95% of analyzed cases.  

**Expected Benefits**:  
- Save time and resources for legal professionals.  
- Provide actionable insights to support legal decision-making.  
- Enhance understanding of complex legal cases through LLM-powered summaries.  

---

### 9. Conclusion  

This project demonstrates the integration of advanced data pipelines, vector databases, and large language models to address challenges in legal document analysis. By automating workflows and enhancing insights, it offers significant value to legal professionals and organizations.

---

## Technology Stack  

- **ETL**: Apache Airflow.  
- **Backend**: FastAPI.  
- **Frontend**: Streamlit.  
- **Data Storage**: Snowflake and Pinecone.  
- **LLMs**: OpenAI GPT-4 and HuggingFace embeddings.  
- **Models**: Scikit-learn and PyTorch-based fraud classifiers.  

---

## Benefits  

1. **Fraud Detection**: Robust analysis using embeddings and LLMs.  
2. **Dispute Analysis**: Accurate categorization and outcome prediction.  
3. **Case Summarization**: Generate concise, user-friendly summaries of legal cases.  
4. **Precedent Retrieval**: Enhanced case retrieval through similarity searches.  
5. **Scalability**: Support for large-scale datasets through Pinecone and LLM integration.  
6. **User-Friendly**: Streamlit provides an intuitive interface for legal professionals.  
