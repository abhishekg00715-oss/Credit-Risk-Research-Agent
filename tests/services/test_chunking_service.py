"""
test_chunking_service.py

Unit tests for Chunking Service.
"""

from pathlib import Path

from src.ingestion.pdf_ingestion_new import PDFIngestion
from src.services.chunking_service import ChunkingService


def test_chunks_created():
    """
    Verify chunks are created from documents.
    """

    ingestion = PDFIngestion(
        policy_path="docs/policies"
    )

    documents = ingestion.load_documents()

    chunking_service = ChunkingService(
        chunk_size=150,
        chunk_overlap=25
    )

    chunks = chunking_service.create_chunks(
        documents
    )

    assert chunks is not None
    assert len(chunks) > 0


def test_chunk_contains_text():
    """
    Verify chunk contains text.
    """

    ingestion = PDFIngestion(
        policy_path="docs/policies"
    )

    documents = ingestion.load_documents()

    chunking_service = ChunkingService(
        chunk_size=150,
        chunk_overlap=25
    )

    chunks = chunking_service.create_chunks(
        documents
    )

    first_chunk = chunks[0]

    assert len(first_chunk.text.strip()) > 0


def test_chunk_metadata_preserved():
    """
    Verify source metadata exists.
    """

    ingestion = PDFIngestion(
        policy_path="docs/policies"
    )

    documents = ingestion.load_documents()

    chunking_service = ChunkingService(
        chunk_size=150,
        chunk_overlap=25
    )

    chunks = chunking_service.create_chunks(
        documents
    )

    first_chunk = chunks[0]

    assert "file_name" in first_chunk.metadata
    assert "source" in first_chunk.metadata


def test_chunk_count_greater_than_documents():
    """
    Verify chunking splits documents.
    """

    ingestion = PDFIngestion(
        policy_path="docs/policies"
    )

    documents = ingestion.load_documents()

    chunking_service = ChunkingService(
        chunk_size=150,
        chunk_overlap=25
    )

    chunks = chunking_service.create_chunks(
        documents
    )

    assert len(chunks) >= len(documents)


def test_chunk_export():
    """
    Verify chunk export file is created.
    """

    ingestion = PDFIngestion(
        policy_path="docs/policies"
    )

    documents = ingestion.load_documents()

    chunking_service = ChunkingService(
        chunk_size=150,
        chunk_overlap=25
    )

    chunks = chunking_service.create_chunks(
        documents
    )

    output_file = (
        "data/chunks/test_policy_chunks.json"
    )

    chunking_service.export_chunks(
        chunks,
        output_file
    )

    assert Path(output_file).exists()
