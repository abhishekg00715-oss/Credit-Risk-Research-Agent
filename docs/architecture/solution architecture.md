# Solution Architecture

## Overview

The Credit Risk Research Agent is a local-first, multi-agent AI platform designed to assist credit analysts in researching lending policies, assessing customer risk, analyzing portfolio trends, and generating explainable recommendations.

The solution is intentionally designed as a personal project and therefore avoids cloud dependencies such as AWS S3, AWS Glue, Redshift, or managed vector databases.

All components execute locally on a developer workstation.

---

# Architecture Goals

The solution aims to:

- Demonstrate Agentic AI concepts
- Demonstrate RAG implementation
- Showcase Credit Risk domain knowledge
- Provide explainable recommendations
- Support future agent expansion
- Operate entirely on local infrastructure

---

# Architecture Principles

1. Local-first execution
2. Explainability over complexity
3. Modular agent design
4. Evidence-based recommendations
5. Extensible architecture
6. Separation of concerns

---

# Technology Stack

| Layer | Technology |
|---------|-----------|
| UI | Streamlit |
| Agent Framework | AISuite |
| LLM Access | OpenAI GPT |
| Orchestration | Coordinator Agent |
| RAG Framework | LlamaIndex |
| Embeddings | Sentence Transformers (Local) |
| Vector Store | ChromaDB |
| Customer Data | SQLite |
| Portfolio Data | CSV / SQLite |
| Configuration | YAML / ENV |
| Logging | Python Logging |
| Language | Python |

---

# High-Level Architecture

```

+-------------------+
| Streamlit UI |
+---------+---------+
|
v
+-------------------+
| Coordinator Agent |
+---------+---------+
|
+-------------------+-------------------+
| | |
v v v

+-----------+ +------------+ +------------+
| Policy | | Customer | | Portfolio |
| Agent | | Agent | | Agent |
+-----+-----+ +------+-----+ +------+-----+
| | |
v v v

+-----------+ +-----------+ +-----------+
| ChromaDB | | SQLite | | Portfolio |
| Policies | | Customer | | Dataset |
+-----------+ +-----------+ +-----------+

|
v

+-------------------+
| Recommendation |
| Agent |
+---------+---------+
|
v

+-------------------+
| Explainability |
| Agent |
+-------------------+

```

---

# Component Description

## Streamlit UI

Responsibilities:

- Accept user requests
- Display responses
- Display citations
- Display recommendations

Examples:

- Ask policy questions
- Assess customer risk
- Analyze portfolio trends

---

## Coordinator Agent

Responsibilities:

- Receive user requests
- Identify workflow
- Route requests to appropriate agents
- Aggregate outputs

The coordinator contains no business logic.

---

## Policy Agent

Responsibilities:

- Policy document retrieval
- Semantic search
- Citation generation
- RAG response generation

Data Source:

- Policy PDFs
- ChromaDB

---

## Customer Agent

Responsibilities:

- Customer lookup
- Credit score analysis
- Income evaluation
- Utilization analysis

Data Source:

- SQLite

---

## Portfolio Agent

Responsibilities:

- Segment analysis
- Default rate analysis
- Trend detection

Data Source:

- Portfolio Dataset

---

## Recommendation Agent

Responsibilities:

- Consolidate findings
- Apply credit rules
- Generate recommendation

Possible Outputs:

- Approve
- Decline
- Review

---

## Explainability Agent

Responsibilities:

- Gather evidence
- Attach citations
- Generate confidence score
- Create decision rationale

---

# Storage Architecture

## Unstructured Data

Policy Documents

Format:

- PDF

Storage:

```text
data/policies/
```

---

## Vector Storage

Embeddings

Storage:

```text
ChromaDB
```

Purpose:

```text
Semantic Search
Similarity Search
RAG Context Retrieval
```

---

## Structured Data

Customer Profiles

Storage:

```text
SQLite
```

Example:

```text
customer.db
```

---

## Analytical Data

Portfolio Metrics

Storage:

```text
portfolio.csv
```

---

# Deployment Model

The initial design of the  solution is intended for local execution. There can be further design improvements which can enable the solution to use cloud services.

Deployment Target:

```text
Developer Laptop
```

Minimum Requirements:

```text
8 GB RAM
Python 3.11+
Internet Access (LLM API Calls)
```

---

# Future Evolution

Future agents may include:

- Regulatory Agent : Monitors and interprets regulatory guidelines to identify impacts on credit risk policies and decision-making.
- Fraud Risk Agent : Detects suspicious customer behaviors and potential fraud indicators during credit assessment.
- Market Intelligence Agent : Analyzes macroeconomic, industry, and market trends that may influence portfolio risk and lending strategies.
- Collections Agent : Evaluates delinquent accounts and recommends collection, recovery, or customer engagement actions.

The architecture is designed to support additional agents without significant redesign.
