"""
policy_agent.py

Policy Agent responsible for
retrieving relevant credit policy
information and generating
context-aware responses using
Retrieval-Augmented Generation (RAG).

Responsibilities

- Receive policy questions
- Retrieve relevant policy chunks
- Build LLM context
- Generate policy response


Author:
Credit Risk Research Agent
"""

from src.services.retrieval_service import (
    RetrievalService
)

from src.services.llm_service import (
    LLMService
)


class PolicyAgent:

    def __init__(self):

        self.retriever = (
            RetrievalService()
        )

        self.llm = (
            LLMService()
        )

    def build_context(
        self,
        retrieval_results
    ) -> str:
        """
        Convert retrieved chunks
        into LLM context.
        """

        documents = (
            retrieval_results["documents"][0]
        )

        metadata = (
            retrieval_results["metadatas"][0]
        )

        context_parts = []

        for idx in range(
            len(documents)
        ):

            context_parts.append(

                f"""
Source:
{metadata[idx]['file_name']}

Content:
{documents[idx]}
"""
            )

        return "\n".join(
            context_parts
        )

    def build_prompt(
        self,
        question: str,
        context: str
    ) -> str:
        """
        Create RAG prompt.
        """

        return f"""
You are a credit policy expert.

Answer the user's question using ONLY the provided policy context.

Important:
• If the question refers to a specific customer, your responsibility is ONLY to explain the applicable policy requirements.
• Do NOT attempt to determine whether the customer satisfies those requirements unless customer information is explicitly present in the provided context.
• Do NOT make recommendations or eligibility decisions.

If the requested policy information is not present in the supplied context, state that clearly.

Question:
{question}

Context:
{context}

Instructions:

1. Summarize the applicable policy.
2. Explain the relevant eligibility or underwriting rules.
3. Cite the source document(s).
4. Do not invent policy rules.
5. Do not evaluate customer eligibility.
"""

    def answer_question(
        self,
        question: str,
        top_k: int = 2
    ):
        """
        End-to-end RAG workflow.
        """

        results = (
            self.retriever.retrieve_chunks(
                query=question,
                top_k=top_k
            )
        )

        context = (
            self.build_context(
                results
            )
        )

        prompt = (
            self.build_prompt(
                question,
                context
            )
        )

        answer = (
            self.llm.generate_response(
                prompt
            )
        )

        return answer

    def process_request(
        self,
        query: str
    ) -> str:
        """
        Standard Coordinator entry point.
        """
    
        return self.answer_question(query)


if __name__ == "__main__":

    agent = PolicyAgent()

    query = (
        "What card is suitable "
        "for a customer with a "
        "credit score of 720?"
    )

    response = (
        agent.process_request(
            query
        )
    )

    print("\n")
    print("=" * 80)
    print("POLICY AGENT RESPONSE")
    print("=" * 80)

    print(response)
