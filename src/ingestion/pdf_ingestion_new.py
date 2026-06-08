"""
pdf_ingestion.py

Purpose:
Load policy PDF documents and convert them
into LlamaIndex Document objects.

Author:
Credit Risk Research Agent
"""

from pathlib import Path
from typing import List

from pypdf import PdfReader
from llama_index.core import Document


class PDFIngestion:
    """
    Handles ingestion of PDF policy documents.
    """

    def __init__(self, policy_path: str):
        self.policy_path = Path(policy_path)

    def load_documents(self) -> List[Document]:
        """
        Load all PDF files and return
        LlamaIndex Document objects.
        """

        documents = []

        pdf_files = list(
            self.policy_path.glob("*.pdf")
        )

        print(
            f"Found {len(pdf_files)} PDF file(s)"
        )

        for pdf_file in pdf_files:

            print(
                f"Processing: {pdf_file.name}"
            )

            reader = PdfReader(pdf_file)

            full_text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    full_text += page_text + "\n"

            document = Document(
                text=full_text,
                metadata={
                    "file_name": pdf_file.name,
                    "source": str(pdf_file)
                }
            )

            documents.append(document)

        print(
            f"Successfully loaded "
            f"{len(documents)} document(s)"
        )

        return documents

    def preview_documents(
        self,
        documents: List[Document],
        preview_length: int = 1000
    ):
        """
        Preview extracted content.
        """

        for idx, doc in enumerate(documents):

            print("\n" + "=" * 80)
            print(
                f"Document {idx + 1}"
            )

            print(
                f"Source: "
                f"{doc.metadata['file_name']}"
            )

            print("=" * 80)

            print(
                doc.text[:preview_length]
            )

    def export_text(
        self,
        documents: List[Document],
        output_dir: str
    ):
        """
        Export extracted text
        for validation/debugging.
        """

        output_path = Path(output_dir)

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        for doc in documents:

            filename = (
                Path(
                    doc.metadata["file_name"]
                ).stem + ".txt"
            )

            with open(
                output_path / filename,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(doc.text)

        print(
            f"Exported documents "
            f"to {output_dir}"
        )


if __name__ == "__main__":

    ingestion = PDFIngestion(
        policy_path="data/policies"
    )

    documents = ingestion.load_documents()

    ingestion.preview_documents(
        documents
    )

    ingestion.export_text(
        documents,
        output_dir="data/processed"
    )
