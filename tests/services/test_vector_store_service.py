from src.services.vector_store_service import (
    VectorStoreService
)


def test_collection_created():

    vector_store = (
        VectorStoreService()
    )

    assert (
        vector_store.collection
        is not None
    )


def test_records_loaded():

    vector_store = (
        VectorStoreService()
    )

    records = (
        vector_store.load_embeddings(
            "data/embeddings/policy_embeddings.json"
        )
    )

    assert len(records) > 0
