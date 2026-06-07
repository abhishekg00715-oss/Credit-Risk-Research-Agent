## <*This is in progress*>

This document defines the quality attributes and operational expectations for the Credit Risk Research Agent. 

Following Non-Functional requirements to be covered by the solution :

# Performance

## Objective
Provide timely responses to user queries without excessive delays.

| ID | Requirement | Target | Priority |
|------|-------------|---------|-------|
| NFR-1 | Policy document query response time | < 10 seconds | should have |
| NFR-2 | Customer profile retrieval time | < 3 seconds | should have |
| NFR-3 | Portfolio analytics response time | < 15 seconds | should have |
| NFR-4 | End-to-end credit assessment workflow | < 20 seconds | should have |



# Accuracy & Relevance

## Objective

Provide contextually relevant and factually grounded responses.


| ID | Requirement | Priority |
|--------|---------------|------|
| NFR-5 | Responses must be generated using retrieved context whenever available | Must have |
| NFR-6 | Policy-related responses should reference source documents | Must have |
| NFR-7 | Hallucinated policy rules should be minimized through retrieval-augmented generation (RAG) | Must have |
| NFR-8 | Recommendations should be derived from available evidence rather than unsupported assumptions | Should have |



# Explainability

## Objective

Ensure that every recommendation can be understood and justified.


| ID | Requirement | Priority |
|------|-------------|-------|
| NFR-9 | All policy answers must include source citations | Must Have |
| NFR-10 | Recommendations must include supporting rationale | Must Have |
| NFR-11 | Evidence used in decision generation must be visible to users | Must Have |
| NFR-12 | Confidence scores should be provided where feasible | Should Have |



# Auditability

## Objective

Enable users to trace how conclusions were generated.



| ID | Requirement | Priority |
|------|-------------|------|
| NFR-13 | User questions should be logged | Should have |
| NFR-14 | Agent responses should be logged | Should have |
| NFR-15 | Retrieved source references should be captured | Should have |
| NFR-16 | Workflow execution history should be traceable | Should have |



# Maintainability

## Objective

Enable future enhancements with minimal redesign.


| ID | Requirement | Priority |
|------|-------------|-------|
| NFR-17 | Agents must follow single-responsibility principles | Must have |
| NFR-18 | Business logic should be separated from UI logic | Should have |
| NFR-19 | Shared services should be reusable across agents | Must have |
| NFR-20 | Configuration should be externalized | Must have |



# Extensibility

## Objective

Allow new agents and capabilities to be added easily.

### Requirements

| ID | Requirement | Priority |
|------|-------------|-----|
| NFR-21 | New agents should be pluggable into the Coordinator Agent | Should have |
| NFR-22 | New document sources should be supported without redesign | Could have |
| NFR-23 | Additional datasets should be onboarded through configuration | Could have |
| NFR-24 | LLM providers should be interchangeable through AISuite | Could have |
