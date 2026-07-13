# Product Backlog

## Epic: Policy Research Assistant

| ID | Feature / User Story | Priority |
|----|----------------------|----------|
| CRA-1 | Upload and ingest policy PDFs | Must |
| CRA-2 | Extract text and chunk documents | Must |
| CRA-3 | Generate embeddings for document chunks | Must |
| CRA-4 | Store embeddings in ChromaDB / FAISS | Must |
| CRA-5 | Implement semantic search over policies | Must |
| CRA-6 | Generate RAG-based answers with citations | Must |

---

## Epic: Customer Risk Assessment

| ID | Feature / User Story | Priority |
|----|----------------------|----------|
| CRA-7 | Customer Data Foundation (SQLite) | Must |
| CRA-8 | Implement customer lookup by customer_id | Must |
| CRA-9 | Calculate credit score assessment | Should |
| CRA-10 | Analyze income and credit utilization | Should |
| CRA-11 | Generate customer risk summary | Should |

---

## Epic: Portfolio Intelligence

| ID | Feature / User Story | Priority |
|----|----------------------|----------|
| CRA-12 | Load portfolio dataset (CSV / SQLite) | Must |
| CRA-13 | Compute default rates by customer segment | Should |
| CRA-14 | Perform trend analysis over time | Should |
| CRA-15 | Identify high-risk segments and risk hotspots | Could |

---

## Epic: Recommendation Engine

| ID | Feature / User Story | Priority |
|----|----------------------|----------|
| CRA-16 | Implement rule evaluation engine | Should |
| CRA-17 | Calculate risk score | Should |
| CRA-18 | Generate recommendation (Approve / Decline / Review) | Should |
| CRA-19 | Generate recommendation rationale | Should |

---

## Epic: Explainability & Governance

| ID | Feature / User Story | Priority |
|----|----------------------|----------|
| CRA-20 | Attach policy citations to responses | Must |
| CRA-21 | Collect supporting evidence from all agents | Should |
| CRA-22 | Generate confidence score | Could |
| CRA-23 | Persist decision trace / audit trail | Could |

---

## Epic: Multi-Agent Orchestration

| ID | Feature / User Story | Priority |
|----|----------------------|----------|
| CRA-24 | Implement Coordinator Agent | Must |
| CRA-25 | Implement Policy Agent | Must |
| CRA-26 | Implement Customer Agent | Must |
| CRA-27 | Implement Portfolio Agent | Must |
| CRA-28 | Implement Recommendation Agent | Must |
| CRA-29 | Implement Explainability Agent | Should |
| CRA-30 | Create end-to-end credit assessment workflow | Should |

---

## Epic: User Experience & Demo

| ID | Feature / User Story | Priority |
|----|----------------------|----------|
| CRA-31 | Build Streamlit UI for Policy Research | Must |
| CRA-32 | Build Streamlit UI for Customer Assessment | Should |
| CRA-33 | Build Streamlit UI for Portfolio Analysis | Should |
| CRA-34 | Add sample queries and demo scenarios | Must |
| CRA-35 | Capture screenshots and walkthroughs for README | Should |

---




# MVP Scope (Release 1.0)

The following backlog items constitute the Minimum Viable Product:

| ID | Feature | status |
|----|---------|--------|
| CRA-1 | Upload and ingest policy PDFs | **Done** |
| CRA-2 | Extract text and chunk documents |**Done**|
| CRA-3 | Generate embeddings |**Done**|
| CRA-4 | Store embeddings |**Done**|
| CRA-5 | Semantic search |**Done**|
| CRA-6 | RAG-based answers with citations |**Done**|
| CRA-20 | Source attribution |**Done**|
| CRA-24 | Coordinator Agent |**Done**|
| CRA-25 | Policy Agent |**Done**|
| CRA-31 | Build Streamlit UI for Policy Research |**Done**|
| CRA-34 | Sample queries and demo scenarios |**Done**|

| ID | NFR | status |
|----|---------|--------|
| NFR-5 | Responses must be generated using retrieved context whenever available |**Done**|
| NFR-6 | Policy-related responses should reference source documents|**Done**|
| NFR-7 | Hallucinated policy rules should be minimized through retrieval-augmented generation (RAG)|**Done**|
| NFR-9 | All policy answers must include source citations | **Done** |
| NFR-17 | Agents must follow single-responsibility principles | **Done** |
| NFR-18 | Business logic should be separated from UI logic | **Done** |
| NFR-19 | Shared services should be reusable across agents |**Done** |
| NFR-21 | New agents should be pluggable into the Coordinator Agent | **Done** |



---


---
# Phase 2 Backlog 

| ID | Feature | status |
|----|---------|--------|
| CRA-7 | Customer Data Foundation (SQLite) | **Done** |
| CRA-8 | Implement customer lookup by customer_id | **Done** |
| CRA-9 | Calculate credit score assessment | **To Do** |
| CRA-10 | Analyze income and credit utilization | **To Do** |
| CRA-11 | Generate customer risk summary | **To Do** |



| ID | NFR | status |
|----|---------|--------|
| NFR-2 | Customer profile retrieval time |**To Do**|
|NFR-8 | Customer recommendations shall be derived from retrieved evidence.|**To Do**|
|NFR-10| Customer assessments shall include supporting rationale.|**To Do**|
|NFR-11| Evidence used to generate customer assessments shall be visible to users.|**To Do**|
|NFR-13| User questions should be logged.|**To Do**|
|NFR-14| Agent responses should be logged.|**To Do**|





