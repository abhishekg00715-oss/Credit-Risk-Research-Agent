"""
app.py

Purpose:
Streamlit user interface for the
Credit Risk Research Agent MVP.

Author:
Credit Risk Research Agent
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

sys.path.append(
    str(PROJECT_ROOT)
)

import streamlit as st

from src.agents.coordinator_agent import (CoordinatorAgent)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Credit Risk Research Agent",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Coordinator Initialization
# --------------------------------------------------

@st.cache_resource
def load_coordinator():

    return CoordinatorAgent()


coordinator = load_coordinator()


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title(
    "📊 Credit Risk Research Agent"
)

st.markdown(
    """
    Ask questions about credit policies,
    underwriting rules, eligibility criteria,
    and risk guidelines.
    """
)


# --------------------------------------------------
# Query Input
# --------------------------------------------------

query = st.text_area(
    "Enter your question:",
    height=120,
    placeholder=(
        "Example:\n"
        "What is the minimum credit score "
        "required for a premium credit card?"
    )
)


# --------------------------------------------------
# Submit Button
# --------------------------------------------------

if st.button(
    "Submit Question"
):

    if not query.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Analyzing policy documents..."
        ):

            try:

                response = (
                    coordinator.process_query(
                        query
                    )
                )

                st.success(
                    "Response Generated"
                )

                st.markdown(
                    "### Answer"
                )

                st.write(
                    response
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )


# --------------------------------------------------
# Sample Questions
# --------------------------------------------------

st.markdown("---")

st.markdown(
    "### Sample Questions"
)

st.markdown(
    """
    - What is the minimum credit score required for a premium credit card?

    - Can a customer with a credit score of 640 be approved?

    - What utilization ratio is considered low risk?

    - What annual income is required for self-employed applicants?

    - What conditions result in automatic decline?
    """
)