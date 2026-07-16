**Phase 1**

Policy Research Assistant

Goal:
Policy Agent-
This agent will allow users to query credit policy documents.

Capabilities:

- PDF ingestion
- Embeddings
- Semantic search
- RAG based responses
- Source retrieval and citation

  
**Phase 2**

Customer Risk Assessment 

Goal:
Build the Customer Risk Assessment capability and establish the Coordinator Agent as the single entry point for customer and policy requests.

Capabilities:

- Customer lookup
- Credit score evaluation
- Income analysis
- Credit utilization analysis
- Customer risk summarization
- Coordinator-based request routing
- Multi-agent request orchestration (Policy + Customer, without synthesis)

**Phase 3**
Portfolio Intelligence

Goal:
Portfolio Agent-
Analyze historical portfolio performance.

Capabilities:

- Segment analysis
- Default rate analysis
- Risk trend detection

**Phase 4**

Recommendation Engine

Goal:
Recommendation Agent - this agent will combine findings from multiple agents.

Capabilities
- Rule evaluation
- Risk scoring
- Recommendation generation
- Decision rationale generation


**Phase 5**
 
 Explainability & Governance
 
 Goal : Explainability Agent - Provide transparent, auditable, and evidence-backed explanations for all recommendations
 
Capabilities
- Source attribution
- Evidence collection
- Confidence score generation
- Decision traceability
- Audit trail generation
 

**Phase 6**

Multi-Agent Workflow

Goal:

To integrate all the agents working together in an End-to-end orchestration.

Policy Agent
+
Customer Agent
+
Portfolio Agent
->
Recommendation Agent
-> Explainability Agent


