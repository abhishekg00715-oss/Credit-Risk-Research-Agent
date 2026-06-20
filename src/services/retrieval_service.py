"""
retrieval_service.py

Purpose:
Perform semantic search against
the policy vector store.

Author:
Credit Risk Research Agent
"""

from typing import List

import chromadb
from sentence_transformers import (
    SentenceTransformer
)


class RetrievalService:
    """
    Semantic search service
    for policy retrieval.
    """

    def __init__(
        self,
        db_path: str = "data/vector_store/chroma_db",
        collection_name: str = "policy_documents",
        model_name: str = "BAAI/bge-small-en-v1.5"
    ):
        """
        Initialize ChromaDB and
        embedding model.
        """

        self.client = chromadb.PersistentClient(
            path=db_path
        )

        self.collection = (
            self.client.get_collection(
                name=collection_name
            )
        )

        self.embedding_model = (
            SentenceTransformer(
                model_name
            )
        )

        print(
            f"Connected to collection: "
            f"{collection_name}"
        )

    def generate_query_embedding(
        self,
        query: str
    ) -> List[float]:
        """
        Generate embedding
        for user query.
        """

        embedding = (
            self.embedding_model.encode(
                query,
                normalize_embeddings=True
            )
        )

        return embedding.tolist()

    def semantic_search(
        self,
        query: str,
        top_k: int = 3
    ):
        """
        Retrieve most relevant chunks.

        Parameters
        ----------
        query : str
            User search query

        top_k : int
            Number of chunks to return
        """

        print(
            "\nPerforming Semantic Search..."
        )

        query_embedding = (
            self.generate_query_embedding(
                query
            )
        )

        results = (
            self.collection.query(
                query_embeddings=[
                    query_embedding
                ],
                n_results=top_k
            )
        )

        return results

    def display_results(
        self,
        results
    ):
        """
        Display retrieval results
        in a readable format.
        """

        documents = (
            results.get(
                "documents",
                [[]]
            )[0]
        )

        metadatas = (
            results.get(
                "metadatas",
                [[]]
            )[0]
        )

        distances = (
            results.get(
                "distances",
                [[]]
            )[0]
        )

        print(
            "\nSearch Results"
        )

        print(
            "=" * 80
        )

        for idx in range(
            len(documents)
        ):

            print(
                f"\nResult {idx + 1}"
            )

            print(
                "-" * 80
            )

            print(
                f"Source: "
                f"{metadatas[idx].get('file_name')}"
            )

            print(
                f"Distance: "
                f"{distances[idx]:.4f}"
            )

            print(
                "\nRetrieved Text:\n"
            )

            print(
                documents[idx]
            )

            print(
                "\n"
                + "=" * 80
            )

    def retrieve_chunks(
        self,
        query: str,
        top_k: int = 3
    ):
        """
        Main retrieval method.

        Returns structured
        search results.
        """

        results = self.semantic_search(
            query=query,
            top_k=top_k
        )

        return results


if __name__ == "__main__":

    retrieval_service = (
        RetrievalService()
    )

    query = (
        "What card is suitable for a customer with a credit score of 720 ?"
    )
    results = (
        retrieval_service.retrieve_chunks(
            query=query,
            top_k=1
        )
    )

    retrieval_service.display_results(
        results
    )