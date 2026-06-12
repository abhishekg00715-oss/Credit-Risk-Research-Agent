"""
vector_store_service.py

Purpose:
Load embeddings into ChromaDB
for semantic retrieval.

Author:
Credit Risk Research Agent
"""

import json
from pathlib import Path

import chromadb
from chromadb.config import Settings


class VectorStoreService:
    """
    Stores policy embeddings
    inside a local ChromaDB collection.
    """

    def __init__(
        self,
        db_path: str = "data/vector_store/chroma_db",
        collection_name: str = "policy_documents"
    ):

        self.db_path = db_path
        self.collection_name = collection_name

        Path(self.db_path).mkdir(
            parents=True,
            exist_ok=True
        )

        self.client = chromadb.PersistentClient(
            path=self.db_path
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=self.collection_name
            )
        )

        print(
            f"Connected to collection: "
            f"{self.collection_name}"
        )

    def load_embeddings(
        self,
        embedding_file: str
    ) -> list:
        """
        Load embedding JSON file.
        """

        with open(
            embedding_file,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        print(
            f"Loaded {len(data)} records"
        )

        return data

    def store_embeddings(
        self,
        embedded_chunks: list
    ):
        """
        Insert embeddings into ChromaDB.
        """

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in embedded_chunks:

            ids.append(
                chunk["chunk_id"]
            )

            documents.append(
                chunk["text"]
            )

            embeddings.append(
                chunk["embedding"]
            )

            metadatas.append(
                {
                    "file_name":
                        chunk["metadata"].get(
                            "file_name",
                            ""
                        ),

                    "source":
                        chunk["metadata"].get(
                            "source",
                            ""
                        ),

                    "chunk_number":
                        chunk.get(
                            "chunk_number",
                            0
                        )
                }
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

        print(
            f"Stored {len(ids)} embeddings"
        )

    def collection_statistics(
        self
    ):
        """
        Display collection metrics.
        """

        count = self.collection.count()

        print(
            "\nVector Store Statistics"
        )

        print(
            f"Collection Name: "
            f"{self.collection_name}"
        )

        print(
            f"Total Records: "
            f"{count}"
        )

    def sample_record(
        self
    ):
        """
        Display sample record.
        """

        result = self.collection.peek(
            limit=1
        )

        print(
            "\nSample Record:"
        )

        print(result)


if __name__ == "__main__":

    vector_store = VectorStoreService()

    embedded_chunks = (
        vector_store.load_embeddings(
            "data/embeddings/policy_embeddings.json"
        )
    )

    vector_store.store_embeddings(
        embedded_chunks
    )

    vector_store.collection_statistics()

    vector_store.sample_record()
