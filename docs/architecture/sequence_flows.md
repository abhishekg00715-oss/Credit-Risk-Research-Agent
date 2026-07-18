# Sequence Flows

<WIP>

## Overview

This document describes the end-to-end execution flows implemented within the Credit Risk Research Agent.

Unlike the Solution Architecture document, which focuses on structural components, this document illustrates how requests travel through the system during runtime.

The documented flows reflect the implementation completed through Phase 2.

---

# Sequence Flow Principles

All execution flows follow the same architectural principles:

- User requests always enter through the Coordinator Agent.
- Business logic remains inside specialist agents.
- The Coordinator performs orchestration only.
- Responses are standardized before presentation.
- Logging occurs independently of business logic.
- Services communicate synchronously.

---

# Flow 1 – Policy Research

## Objective

Answer policy-related questions using Retrieval-Augmented Generation (RAG).

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Coordinator Agent
 │
 ▼
Intent Routing Service
 │
 ▼
Policy Agent
 │
 ▼
Retrieval Service
 │
 ▼
ChromaDB
 │
 ▼
Relevant Policy Chunks
 │
 ▼
Policy Agent
 │
 ▼
LLM Service
 │
 ▼
OpenAI
 │
 ▼
Generated Policy Answer
 │
 ▼
Response Formatting Service
 │
 ▼
Streamlit UI
```

---

# Flow 2 – Customer Assessment

## Objective

Retrieve and assess a customer's credit profile.

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Coordinator Agent
 │
 ▼
Intent Routing Service
 │
 ▼
Customer Agent
 │
 ▼
Customer Repository
 │
 ▼
SQLite Database
 │
 ▼
Customer Profile
 │
 ▼
Customer Assessment Service
 │
 ▼
Business Rule Evaluation
 │
 ▼
Customer Summary Service
 │
 ▼
Risk Summary
 │
 ▼
Response Formatting Service
 │
 ▼
Streamlit UI
```

---

# Flow 3 – Policy + Customer Assessment

## Objective

Evaluate a customer against a lending policy.

Current implementation invokes both specialist agents independently before combining their outputs.

```text
                        User
                          │
                          ▼
                  Coordinator Agent
                          │
                Intent Routing Service
          ┌───────────────┴───────────────┐
          ▼                               ▼
   Policy Agent                    Customer Agent
          │                               │
          ▼                               ▼
 Retrieval Service              Customer Repository
          │                               │
          ▼                               ▼
     LLM Service            Assessment Service
                                          │
                                          ▼
                               Summary Service
          └───────────────┬───────────────┘
                          ▼
            Response Formatting Service
                          ▼
                   Streamlit UI
```

**Current Behaviour**

- Both agents execute independently.
- No inter-agent communication occurs.
- The Coordinator aggregates both responses.
- The Response Formatting Service presents a consolidated view.

---

# Logging Flow

Every request generates two independent audit trails.

```text
User Query
     │
     ▼
Coordinator
     │
     ├────────► Query Logger
     │
     ▼
Agent Invocation
     │
     ▼
Agent Execution Logger
     │
     ▼
JSON Log Files
```

Generated artifacts:

- query_log.json
- agent_execution_log.json

---

# Error Handling Flow

Errors are isolated to the component in which they occur.

```text
Agent
 │
Exception
 │
 ▼
Coordinator
 │
 ▼
Standardized Error Response
 │
 ▼
Response Formatting Service
 │
 ▼
Streamlit UI
```

This prevents infrastructure exceptions from leaking into the presentation layer.

---

# Current Runtime Characteristics

| Characteristic | Current Implementation |
|----------------|------------------------|
| Orchestration | Coordinator Agent |
| Routing | IntentRoutingService |
| Policy Processing | Retrieval + LLM |
| Customer Processing | Rule-Based Assessment |
| Response Formatting | ResponseFormattingService |
| Logging | QueryLogger + AgentExecutionLogger |
| Agent Communication | None |
| Parallel Execution | Not implemented |
| Agent Memory | Not implemented |

---

# Future Sequence Flows

The following execution flows are planned for future phases.

## Portfolio Assessment

```text
Coordinator
        │
        ▼
Portfolio Agent
        │
        ▼
Portfolio Repository
        │
        ▼
Portfolio Analytics
```

---

## Credit Recommendation

```text
Policy Findings
        │
Customer Assessment
        │
Portfolio Insights
        │
        ▼
Recommendation Agent
        │
        ▼
Recommendation
```

---

## Explainability

```text
Recommendation
       │
       ▼
Explainability Agent
       │
       ▼
Evidence Aggregation
       │
       ▼
Final Explainable Decision
```

---

# Planned Evolution

The runtime workflow will continue to evolve as additional capabilities are introduced.

Planned enhancements include:

- Intelligent SLM-based Intent Classification
- Dynamic Agent Registry
- Multi-Agent Workflow Chaining
- Agent Memory
- Confidence Scoring
- Parallel Agent Execution
- Execution Monitoring Dashboard
- Workflow Visualization
