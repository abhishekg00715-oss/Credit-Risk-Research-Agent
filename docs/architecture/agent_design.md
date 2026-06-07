# Agent Design

## Overview

The Credit Risk Research Agent follows a multi-agent architecture where each agent owns a specific business capability and collaborates through a Coordinator Agent.

The design follows the principles of:

* Single Responsibility
* Modularity
* Explainability
* Extensibility

---

# Agent Landscape

```text
                    User
                      │
                      ▼
              Coordinator Agent
                      │
    ┌─────────────────┼─────────────────┐
    ▼                 ▼                 ▼

Policy Agent    Customer Agent    Portfolio Agent

    └─────────────────┼─────────────────┘
                      ▼

            Recommendation Agent
                      ▼

            Explainability Agent
                      ▼

                Final Response
```

---

# Coordinator Agent

## Purpose

Acts as the central orchestrator for all user requests.

## Responsibilities

* Receive user requests
* Identify the required workflow
* Invoke relevant agents
* Aggregate agent outputs
* Return consolidated results

## Inputs

* User query

## Outputs

* Workflow execution result

## Data Access

None

---

# Policy Agent

## Purpose

Provides policy research and retrieval capabilities using RAG.

## Responsibilities

* Search policy documents
* Retrieve relevant policy content
* Generate policy-based answers
* Provide source citations

## Inputs

* Policy-related questions

## Outputs

* Policy findings
* Supporting citations

## Data Sources

* PDF Documents
* ChromaDB

---

# Customer Agent

## Purpose

Evaluates customer creditworthiness using customer profile information.

## Responsibilities

* Retrieve customer information
* Analyze credit score
* Review income profile
* Evaluate credit utilization
* Generate customer risk summary

## Inputs

* Customer ID
* Customer profile data

## Outputs

* Customer risk assessment
* Key strengths
* Key concerns

## Data Sources

* SQLite Customer Database

---

# Portfolio Agent

## Purpose

Provides portfolio-level risk insights and benchmarking.

## Responsibilities

* Analyze customer segments
* Evaluate default trends
* Identify risk hotspots
* Generate portfolio insights

## Inputs

* Portfolio datasets

## Outputs

* Segment performance
* Portfolio risk insights

## Data Sources

* Portfolio CSV Files
* SQLite (future)

---

# Recommendation Agent

## Purpose

Generates a consolidated credit recommendation.

## Responsibilities

* Combine findings from all agents
* Apply business rules
* Calculate risk score
* Generate recommendation

## Inputs

* Policy findings
* Customer assessment
* Portfolio insights

## Outputs

* Approve
* Decline
* Review

## Example Output

```text
Recommendation: Approve

Reason:
- Policy criteria satisfied
- Customer risk acceptable
- Portfolio segment performing well
```

---

# Explainability Agent

## Purpose

Provides transparency and justification for recommendations.

## Responsibilities

* Collect supporting evidence
* Gather source references
* Generate decision rationale
* Calculate confidence score

## Inputs

* Recommendation
* Agent findings
* Citations

## Outputs

* Evidence package
* Confidence score
* Explainable recommendation

## Example Output

```text
Recommendation: Approve

Evidence:
- Policy Section 4.2 satisfied
- Credit Score = 735
- Portfolio Default Rate = 1.2%

Confidence: 88%
```

---

# Agent Interaction Matrix

| Agent                | Consumes                  | Produces             |
| -------------------- | ------------------------- | -------------------- |
| Coordinator Agent    | User Query                | Workflow Execution   |
| Policy Agent         | Policy Questions          | Policy Findings      |
| Customer Agent       | Customer Data             | Risk Assessment      |
| Portfolio Agent      | Portfolio Data            | Portfolio Insights   |
| Recommendation Agent | Agent Findings            | Recommendation       |
| Explainability Agent | Recommendation & Evidence | Explainable Response |

---

# Future Agents

| Agent                     | Purpose                                                                  |
| ------------------------- | ------------------------------------------------------------------------ |
| Regulatory Agent          | Evaluate impacts of regulatory changes on lending policies               |
| Fraud Risk Agent          | Detect potential fraud indicators during assessment                      |
| Market Intelligence Agent | Analyze economic and market trends affecting credit risk                 |
| Collections Agent         | Provide recovery and collections recommendations for delinquent accounts |

---

# Design Principles

1. Each agent owns a single business capability.
2. Agents communicate only through the Coordinator Agent.
3. Business logic remains isolated within individual agents.
4. Recommendations must be evidence-based and explainable.
5. New agents can be added without redesigning existing agents.
6. All agents support local execution without cloud dependencies.

