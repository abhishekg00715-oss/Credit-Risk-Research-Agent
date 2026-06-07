"""
pdf_ingestion.py

Purpose:
Load policy PDF documents and prepare them for
downstream chunking and embedding generation.

Author:
Credit Risk Research Agent Project
"""

from pathlib import Path
from typing import List

from llama_index.core import Document
from llama_index.core import SimpleDirectoryReader


class PDFIngestion:
    """
    Handles loading of policy documents from PDF files.
    """

    def __init__(self, policy_path: str):
        self.policy_path = policy_path

    def load_documents(self) -> List[Document]:
        """
        Load all PDF documents from the configured directory.

        Returns:
            List[Document]
        """

        documents = SimpleDirectoryReader(
            input_dir=self.policy_path,
            required_exts=[".pdf"]
        ).load_data()

        print(f"Loaded {len(documents)} document(s).")

        return documents

    def export_text(
        self,
        documents: List[Document],
        output_dir: str
    ) -> None:
        """
        Optional helper for debugging.

        Saves extracted document text to .txt files.
        """

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        for idx, doc in enumerate(documents):

            file_name = f"document_{idx+1}.txt"

            with open(
                output_path / file_name,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(doc.text)

        print(
            f"Exported {len(documents)} text file(s) "
            f"to {output_dir}"
        )


if __name__ == "__main__":

    ingestor = PDFIngestion(
        policy_path="data/policies"
    )

    docs = ingestor.load_documents()

    ingestor.export_text(
        documents=docs,
        output_dir="data/processed"
    )

    print("\nSample Document Preview:\n")

    print(docs[0].text[:1000])
