## <*This is in progress*>

This document defines the quality attributes and operational expectations for the Credit Risk Research Agent. 

Following Non-Functional requirements to be covered by the solution :

## Performance

| ID | Requirement | Target | Priority | Phase | Status |
|---|---|---|---|---|---|
| NFR-1 | Policy document query response time | < 10 seconds | Should Have | Phase 1 | 🟡 Not Measured |
| NFR-2 | Customer profile retrieval time | < 3 seconds | Should Have | Phase 2 | 🟡 To be validated in CRA-09 |
| NFR-3 | Portfolio analytics response time | < 15 seconds | Should Have | Phase 3 | ⚪ Planned |
| NFR-4 | End-to-end credit assessment workflow | < 20 seconds | Should Have | Phase 5 | ⚪ Planned |

## Accuracy & Relevance
| ID | Requirement | Priority | Phase | Status |
|---|---|---|---|---|
| NFR-5 | Responses shall be generated using retrieved context whenever available. | Must Have | Phase 1 | ✅ Implemented |
| NFR-6 | Policy-related responses shall reference source documents. | Must Have | Phase 1 | ✅ Implemented |
| NFR-7 | Hallucinated policy rules shall be minimized through RAG. | Must Have | Phase 1 | ✅ Implemented |
| NFR-8 | Customer recommendations shall be derived from retrieved evidence. | Should Have | Phase 2 | ⚪ Planned |

## Explainability
| ID | Requirement | Priority | Phase | Status |
|---|---|---|---|---|
| NFR-9 | All policy answers shall include source citations. | Must Have | Phase 1 | ✅ Implemented |
| NFR-10 | Customer assessments shall include supporting rationale. | Must Have | Phase 2 | ⚪ Planned |
| NFR-11 | Evidence used to generate customer assessments shall be visible to users. | Must Have | Phase 2 | ⚪ Planned |
| NFR-12 | Confidence scores should be provided where feasible. | Should Have | Future | ⚪ Deferred |

## Auditability
| ID | Requirement | Priority | Phase | Status |
|---|---|---|---|---|
| NFR-13 | User questions should be logged. | Should Have | Phase 2 | ⚪ Planned |
| NFR-14 | Agent responses should be logged. | Should Have | Phase 2 | ⚪ Planned |
| NFR-15 | Retrieved source references should be captured for audit purposes. | Should Have | Phase 2 | 🟡 Partially Implemented |
| NFR-16 | Multi-agent workflow execution history should be traceable. | Should Have | Phase 5 | ⚪ Planned |

## Maintainability
| ID | Requirement | Priority | Phase | Status |
|---|---|---|---|---|
| NFR-17 | Components shall follow SRP. | Must Have | Phase 1 | ✅ Implemented |
| NFR-18 | Business logic shall be separated from presentation logic. | Must Have | Phase 1 | ✅ Implemented |
| NFR-19 | Shared services shall be reusable across agents. | Must Have | Phase 1 | ✅ Implemented |
| NFR-20 | Configuration shall be externalized from application logic. | Must Have | Phase 1 | 🟡 Partially Implemented |

## Extensibility
| ID | Requirement | Priority | Phase | Status |
|---|---|---|---|---|
| NFR-21 | New agents shall be pluggable into the Coordinator Agent. | Should Have | Phase 1 | ✅ Implemented |
| NFR-22 | New document sources shall be supported with minimal changes. | Could Have | Future | ⚪ Planned |
| NFR-23 | Additional datasets shall be onboarded through configuration. | Could Have | Future | ⚪ Planned |
| NFR-24 | LLM providers shall be interchangeable through AISuite. | Could Have | Future | ⚪ Planned |

## Portability
| ID | Requirement | Priority | Phase | Status |
|---|---|---|---|---|
| NFR-25 | Execute locally without cloud-hosted AI services. | Must Have | Phase 1 | ✅ Implemented |
| NFR-26 | Use lightweight local storage technologies. | Must Have | Phase 1 | ✅ Implemented |
| NFR-27 | Support standard Python runtime and open-source libraries. | Must Have | Phase 1 | ✅ Implemented |
| NFR-28 | Deploy on Windows without enterprise middleware. | Should Have | Phase 1 | ✅ Implemented |

## Data Integrity
| ID | Requirement | Priority | Phase | Status |
|---|---|---|---|---|
| NFR-29 | Validate input documents before ingestion. | Must Have | Phase 1 | 🟡 Partially Implemented |
| NFR-30 | Validate synthetic customer data before loading. | Must Have | Phase 2 | ✅ Implemented |
| NFR-31 | Maintain referential integrity across customer datasets. | Must Have | Phase 2 | ✅ Implemented |





