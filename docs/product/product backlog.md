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
| CRA-7 | Create local customer database (SQLite) | Must |
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

| ID | Feature |
|----|---------|
| CRA-1 | Upload and ingest policy PDFs |
| CRA-2 | Extract text and chunk documents |
| CRA-3 | Generate embeddings |
| CRA-4 | Store embeddings |
| CRA-5 | Semantic search |
| CRA-6 | RAG-based answers with citations |
| CRA-20 | Source attribution |
| CRA-24 | Coordinator Agent |
| CRA-25 | Policy Agent |
| CRA-31 | Streamlit UI |
| CRA-34 | Sample queries and demo scenarios |

---


---
