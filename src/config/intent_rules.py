"""
intent_rules.py

Purpose
-------
Central configuration for deterministic
intent classification used by the
Intent Routing Service.

Responsibilities
----------------
- Define policy intent vocabulary
- Define customer intent vocabulary
- Define customer identifier pattern

Future Enhancements
-------------------
- Portfolio intent vocabulary
- Recommendation intent vocabulary
- Explainability intent vocabulary
- External YAML / JSON configuration

Author
------
Credit Risk Research Agent
"""

# ---------------------------------------------------------
# Customer Identifier
# ---------------------------------------------------------

CUSTOMER_ID_PATTERN = (
    r"\bCUST\d{6}\b"
)

# ---------------------------------------------------------
# Policy Intent Vocabulary
# ---------------------------------------------------------

POLICY_LANGUAGE = {

    "required",
    "minimum",
    "maximum",
    "criteria",
    "eligibility",
    "conditions",
    "approved",
    "approval",
    "decline",
    "policy",
    "guideline",
    "threshold",
    "qualify",
    "eligible"

}

POLICY_SUBJECTS = {

    "credit score",
    "utilization ratio",
    "annual income",
    "income",
    "ltv",
    "dti",
    "debt-to-income",
    "premium credit card",
    "self-employed",
    "repayment history",
    "loan amount"

}

# ---------------------------------------------------------
# Customer Intent Vocabulary
# ---------------------------------------------------------

CUSTOMER_INTENT = {

    "assess",
    "assessment",

    "retrieve",
    "lookup",
    "find",

    "show",
    "display",

    "summarize",

    "analyse",
    "analyze",

    "evaluate",

    "customer profile",

    "risk summary"

}