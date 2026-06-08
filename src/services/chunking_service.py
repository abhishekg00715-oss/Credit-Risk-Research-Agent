"""
chunking_service.py

Purpose:
Split documents into smaller chunks
for embedding generation and retrieval.

Author:
Credit Risk Research Agent
"""

from typing import List

from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter


class ChunkingService:
    """
    Converts documents into chunks (nodes)
    suitable for vector storage.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 50
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.splitter = SentenceSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def create_chunks(
        self,
        documents: List[Document]
    ):
        """
        Convert documents into chunks.

        Returns:
            List[TextNode]
        """

        chunks = self.splitter.get_nodes_from_documents(
            documents
        )

        print(
            f"Created {len(chunks)} chunk(s)"
        )

        return chunks

    def preview_chunks(
        self,
        chunks,
        num_chunks: int = 3
    ):
        """
        Display sample chunks.
        """

        print("\nChunk Preview")

        for idx, chunk in enumerate(
            chunks[:num_chunks]
        ):

            print("\n" + "=" * 80)

            print(
                f"Chunk {idx + 1}"
            )

            print("=" * 80)

            print(
                chunk.text
            )

            print(
                f"\nLength: "
                f"{len(chunk.text)} chars"
            )

    def chunk_statistics(
        self,
        chunks
    ):
        """
        Display chunk metrics.
        """

        lengths = [
            len(chunk.text)
            for chunk in chunks
        ]

        print("\nChunk Statistics")

        print(
            f"Total Chunks: {len(chunks)}"
        )

        print(
            f"Min Length: {min(lengths)}"
        )

        print(
            f"Max Length: {max(lengths)}"
        )

        print(
            f"Average Length: "
            f"{sum(lengths)/len(lengths):.2f}"
        )


if __name__ == "__main__":

    from src.ingestion.pdf_ingestion import PDFIngestion

    ingestion = PDFIngestion(
        policy_path="data/policies"
    )

    documents = ingestion.load_documents()

    chunking_service = ChunkingService(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = chunking_service.create_chunks(
        documents
    )

    chunking_service.preview_chunks(
        chunks
    )

    chunking_service.chunk_statistics(
        chunks
    )
