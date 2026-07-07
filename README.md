# Credit-Risk-Research-Agent
An AI-powered multi-agent decision support platform that enables credit analysts and underwriters to quickly interpret underwriting policies, retrieve relevant policy clauses through semantic search, and generate grounded answers using Retrieval-Augmented Generation (RAG).

The project demonstrates how Generative AI, Vector Databases, and Agentic AI can be applied to enterprise credit risk decision support.

# Business Problem

Financial institutions maintain hundreds of underwriting and policy documents covering credit cards, personal loans, mortgages, fraud, compliance, and regulatory requirements.

Searching these documents manually is:

- Time consuming
- Inconsistent across analysts
- Difficult for new employees
- Prone to interpretation errors

This project provides an AI-powered assistant capable of understanding policy documents and answering underwriting questions using policy-grounded responses with source attribution.

# Key Features 

Current MVP has following features implemented:

 - PDF Policy Ingestion
 - Intelligent Document Chunking
 - Local Embedding Generation
 - ChromaDB Vector Store
 - Semantic Search
 - Retrieval-Augmented Generation (RAG)
 - Policy Agent
 - Coordinator Agent
 - Streamlit User Interface
 - Source Attribution
 - Explainable Responses

# High Level Architecture 

<img width="2048" height="1152" alt="Architecture_diagram" src="https://github.com/user-attachments/assets/0f58bdfe-4a68-4861-8d65-22650a2f6fb4" />

***Note: Further agents will be added into the 'AI ORCHESTRATION LAYER'***

# Technology Stack

| Layer	| Technology |
|--------|-----------------|
|Language|	Python|
|LLM	|OpenAI GPT|
|Embeddings |	Sentence Transformers (Local)|
|Vector Database |	ChromaDB |
|RAG Framework	| LlamaIndex
|UI	|Streamlit|
|Development |	GitHub Codespaces |


# End-to-End Workflow 

Current MVP has the following workflow to be followed:

- Upload policy PDF documents.
- Extract document text.
- Split documents into semantic chunks.
- Generate embeddings locally.
- Store vectors in ChromaDB.
- Perform semantic retrieval.
- Pass retrieved context to the Policy Agent.
- Generate grounded responses using OpenAI GPT.
- Display answers and citations in the Streamlit UI.

# Design Decisions
- Local embedding generation to minimize API cost.
- OpenAI GPT used only for final answer generation.
- ChromaDB selected as an embedded vector database suitable for MVP development.
- Multi-agent architecture separates orchestration from policy reasoning.
- Source attribution included to improve explainability and trust.

# Future Roadmap

Policy agent and Co-ordinator agent are completed and in working state, as part of Phase 1 milestone and MVP.
Future components to be integrated are as follows:

- Customer Agent
- Portfolio Agent
- Fraud Detection Agent
- Recommendation Agent
- Decision Agent
- Loan Agent
- Regulatory Compliance Agent
- Multi-document comparison
- Conversational memory
- AWS deployment (Design and Roadmap)
- CI/CD pipeline

*More details can be referred in the Product Roadmap -docs/product/product roadmap.md*

# How to Run
- Clone the repository.
- Install dependencies.
- Configure the .env file with your OpenAI API key.
- Run the ingestion pipeline.(one time)
- Generate chunks.(one time)
- Generate embeddings.(one time)
- Build the vector store.(one time)
- Launch the Streamlit application.
- streamlit run src/ui/app.py
