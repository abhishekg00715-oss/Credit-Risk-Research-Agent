"""
embedding_service.py

Purpose:
Generate embeddings for policy chunks
using a local embedding model.

Author:
Credit Risk Research Agent
"""

import json
from pathlib import Path
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Generates embeddings
    for chunked policy documents.
    """

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5"
    ):

        print(
            f"Loading embedding model: "
            f"{model_name}"
        )

        self.model = SentenceTransformer(
            model_name
        )

    def load_chunks(
        self,
        chunk_file: str
    ):

        with open(
            chunk_file,
            "r",
            encoding="utf-8"
        ) as file:

            chunks = json.load(file)

        print(
            f"Loaded {len(chunks)} chunks"
        )

        return chunks

    def generate_embeddings(
        self,
        chunks: list
    ):

        print(
            "\nGenerating embeddings..."
        )

        for idx, chunk in enumerate(chunks):

            embedding = self.model.encode(
                chunk["text"],
                normalize_embeddings=True
            )

            chunk["embedding"] = (
                embedding.tolist()
            )

            if (idx + 1) % 5 == 0:

                print(
                    f"Processed "
                    f"{idx + 1} chunks"
                )

        return chunks

    def export_embeddings(
        self,
        chunks: list,
        output_file: str
    ):

        output_path = Path(
            output_file
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                chunks,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"\n✓ Embeddings exported"
        )

        print(
            f"✓ Output: {output_file}"
        )


if __name__ == "__main__":

    embedding_service = (
        EmbeddingService()
    )

    chunks = (
        embedding_service.load_chunks(
            "data/chunks/policy_chunks.json"
        )
    )

    embedded_chunks = (
        embedding_service.generate_embeddings(
            chunks
        )
    )

    embedding_service.export_embeddings(
        embedded_chunks,
        "data/embeddings/policy_embeddings.json"
    )
