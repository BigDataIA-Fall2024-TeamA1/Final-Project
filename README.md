# Final Project





---
Contribution Breakdown:
- Chiu Meng Che: 34%
- Shraddha Bhandarkar: 33%
- Kefan Zhang: 33%


---

## Project Overview

### 1. Introduction  

**Background**:  
This project addresses inefficiencies in legal document management and analysis by leveraging modern data processing pipelines and machine learning models to enhance fraud detection, dispute categorization, and decision-making.  

**Objective**:  
Develop an end-to-end system that automates data ingestion, preprocessing, and legal document analysis, enabling users to interact with results through an intuitive application.  

---

### 2. Scope  

**Boundaries**:  
- **Data Sources**: CourtListener API for legal documents.  
- **Technologies**: Apache Airflow, FastAPI, Streamlit, Pinecone, OpenAI GPT-4, and Snowflake.  
- **Deliverables**: A fully functional application with a backend API, ETL pipeline, and an interactive front-end interface.

**Stakeholders**:  
- Legal professionals seeking insights from past cases.  
- Organizations aiming to enhance fraud detection and dispute resolution processes.

---

### 3. Problem Statement  

**Current Challenges**:  
- Manual analysis of legal documents is time-intensive and prone to errors.  
- Limited tools for automated fraud detection and dispute categorization.  

**Opportunities**:  
- Streamlined legal analysis using AI-powered automation.  
- Improved decision-making with detailed case summaries and recommendations.  

---

### 4. Methodology  

**Data Sources**:  
- CourtListener API or scraped legal documents.  

**Technologies and Tools**:  
- **ETL**: Apache Airflow.  
- **Backend**: FastAPI for API management.  
- **Frontend**: Streamlit for user interaction.  
- **Data Storage**: Snowflake for structured data and Pinecone for vector embeddings.  
- **Models**: OpenAI GPT-4, HuggingFace embeddings, and fraud detection classifiers.  

**Data Pipeline Design**:  
1. **Ingestion**: Automate fetching and storing raw data.  
2. **Preprocessing**: Clean text, extract metadata, generate embeddings, and add fraud labels.  
3. **Storage**: Store raw and processed data in appropriate databases.  

**Data Processing and Transformation**:  
- Use Python-based EDA to explore data and ensure quality transformations.  
- Convert legal text into embeddings for similarity search and categorization.

---

### 5. Project Plan and Timeline  

**Milestones and Deliverables**:  
1. **Week 1-2**: Data ingestion pipeline setup with Apache Airflow.  
2. **Week 3-4**: Preprocessing scripts for text cleaning and embedding generation.  
3. **Week 5**: Pinecone integration for similarity search.  
4. **Week 6**: Backend API development with FastAPI.  
5. **Week 7**: Frontend dashboard implementation with Streamlit.  
6. **Week 8**: Testing and deployment on a cloud platform.  

**Timeline**:  
- Detailed timeline is available in the GitHub Project section.  

---

### 6. Resources and Team  

**Personnel**:  
- **Member 1**: Backend development and API integration.  
- **Member 2**: Frontend development and user interface design.  
- **Member 3**: ETL pipeline and model implementation.  

---

### 7. Risks and Mitigation Strategies  

**Potential Risks**:  
1. Inconsistent or missing data from external APIs.  
2. Integration challenges between components (ETL, backend, frontend).  

**Mitigation Strategies**:  
- Perform data quality checks during ingestion.  
- Use containerization (Docker) to ensure seamless integration.  

---

### 8. Expected Outcomes and Benefits  

**Measurable Goals**:  
- Automate ingestion and preprocessing for at least 90% of incoming legal documents.  
- Achieve over 80% accuracy in fraud detection and dispute categorization.  

**Expected Benefits**:  
- Save time and resources for legal professionals.  
- Provide actionable insights to support legal decision-making.  

---

### 9. Conclusion  

This project demonstrates the integration of advanced data pipelines and machine learning models to address challenges in legal document analysis. By automating workflows and enhancing insights, it offers significant value to legal professionals and organizations.  

---

## Technology Stack  

- **ETL**: Apache Airflow.  
- **Backend**: FastAPI.  
- **Frontend**: Streamlit.  
- **Data Storage**: Snowflake and Pinecone.  
- **Models**: OpenAI GPT-4, HuggingFace embeddings, and scikit-learn-based classifiers.  

---

## Benefits  

1. **Fraud Detection**: Robust analysis using embeddings and classifiers.  
2. **Dispute Analysis**: Accurate categorization and outcome prediction.  
3. **Precedent Retrieval**: Enhanced case retrieval with summaries.  
4. **Scalability**: Support for large-scale datasets.  
5. **User-Friendly**: Streamlit provides an accessible interface.  
