"""
Unit tests for retrieval service.
"""

from src.services.retrieval_service import (
    RetrievalService
)


def test_query_embedding_created():

    retrieval = RetrievalService()

    embedding = (
        retrieval.generate_query_embedding(
            "credit score policy"
        )
    )

    assert embedding is not None
    assert len(embedding) > 0


def test_search_returns_results():

    retrieval = RetrievalService()

    results = (
        retrieval.retrieve_chunks(
            query="minimum credit score",
            top_k=2
        )
    )

    assert results is not None