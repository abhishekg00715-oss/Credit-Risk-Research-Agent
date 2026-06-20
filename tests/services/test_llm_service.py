"""
test_llm_service.py

Smoke tests for LLM Service.
"""

from src.services.llm_service import LLMService


def test_llm_initialization():

    llm = LLMService()

    assert llm.client is not None


def test_simple_completion():

    llm = LLMService()

    response = llm.generate_response(
        prompt="""
        Answer with only one word.

        Question:
        What is 2 + 2?
        """
    )

    assert response is not None
    assert len(response) > 0

    print("\nResponse:")
    print(response)


if __name__ == "__main__":

    test_llm_initialization()

    test_simple_completion()

    print(
        "\n✓ LLM Service Tests Passed"
    )