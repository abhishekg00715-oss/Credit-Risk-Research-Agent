
"""
test_pdf_ingestion.py

Unit tests for PDF ingestion service.
"""

from src.ingestion.pdf_ingestion_new import PDFIngestion


def test_documents_loaded():
    """
    Verify documents are loaded.
    """

    ingestion = PDFIngestion(
        policy_path="docs/policies"
    )

    documents = ingestion.load_documents()

    assert documents is not None
    assert len(documents) > 0


def test_document_contains_text():
    """
    Verify extracted documents contain text.
    """

    ingestion = PDFIngestion(
        policy_path="docs/policies"
    )

    documents = ingestion.load_documents()

    first_doc = documents[0]

    assert len(first_doc.text.strip()) > 0


def test_document_has_metadata():
    """
    Verify metadata is populated.
    """

    ingestion = PDFIngestion(
        policy_path="docs/policies"
    )

    documents = ingestion.load_documents()

    first_doc = documents[0]

    assert "file_name" in first_doc.metadata
    assert "source" in first_doc.metadata