"""
policy_agent.py

Purpose:
Answer policy questions using
retrieval augmented generation.

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

Answer the user's question
using ONLY the provided context.

If information is not found,
say so clearly.

Question:
{question}

Context:
{context}

Instructions:

1. Provide a concise answer.
2. Explain reasoning.
3. Cite source document names.
4. Do not invent policy rules.
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
