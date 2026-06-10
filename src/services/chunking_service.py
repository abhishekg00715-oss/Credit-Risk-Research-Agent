"""
chunking_service.py

Purpose:
Split documents into smaller chunks
for embedding generation and retrieval.

Author:
Credit Risk Research Agent
"""
import json
from typing import List
from pathlib import Path
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import TextNode


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
    ) -> List[TextNode]:
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


    def preview_chunks(
        self,
        chunks: List[TextNode],
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
    
            print(
                f"Node ID: {chunk.node_id}"
            )
    
            print(
                f"Source: "
                f"{chunk.metadata.get('file_name', 'Unknown')}"
            )
    
            print("=" * 80)
    
            print(chunk.text)
    
            print(
                f"\nLength: "
                f"{len(chunk.text)} chars"
        )

    def chunk_statistics(
        self,
        chunks: List[TextNode]
    ):
        """
        Display chunk metrics.
        """
    
        if not chunks:
    
            print(
                "\nNo chunks available."
            )
    
            return
    
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
        
    def export_chunks(
        self,
        chunks: List[TextNode],
        output_file: str
    ):
        """
        Export chunks to JSON file.
    
        Parameters:
            chunks:
                List of TextNodes
    
            output_file:
                Destination JSON file
        """
    
        try:
    
            output_path = Path(output_file)
    
            output_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )
    
            serializable_chunks = []
    
            for idx, chunk in enumerate(chunks):
    
                serializable_chunks.append(
                    {
                        "chunk_id":
                            getattr(
                                chunk,
                                "node_id",
                                f"chunk_{idx}"
                            ),
    
                        "text":
                            chunk.text,
    
                        "metadata":
                            getattr(
                                chunk,
                                "metadata",
                                {}
                            )
                    }
                )
    
            with open(
                output_path,
                "w",
                encoding="utf-8"
            ) as file:
    
                json.dump(
                    serializable_chunks,
                    file,
                    indent=4,
                    ensure_ascii=False
                )
    
            print(
                f"\n✓ Successfully exported "
                f"{len(chunks)} chunks"
            )
    
            print(
                f"✓ Output File: "
                f"{output_file}"
            )
    
        except Exception as e:
    
            print(
                "\n❌ Failed to export chunks"
            )
    
            print(
                f"Reason: {str(e)}"
            )

if __name__ == "__main__":

    from src.ingestion.pdf_ingestion_new import PDFIngestion

    ingestion = PDFIngestion(
        policy_path="docs/policies"
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

    chunking_service.export_chunks(
        chunks,
        output_file="data/chunks/policy_chunks.json"
    )
