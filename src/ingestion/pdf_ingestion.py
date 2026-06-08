"""
pdf_ingestion.py

Purpose:
Load policy documents from Markdown files
for downstream chunking and embedding.

Author:
Credit Risk Research Agent
"""

from pathlib import Path
from typing import List

from llama_index.core import Document
from llama_index.core import SimpleDirectoryReader


class PolicyDocumentIngestion:

    def __init__(self, policy_path: str):
        self.policy_path = policy_path

    def load_documents(self) -> List[Document]:
        """
        Load markdown policy documents.
        """

        documents = SimpleDirectoryReader(
            input_dir=self.policy_path,
            required_exts=[".md"]
        ).load_data()

        print(
            f"Successfully loaded "
            f"{len(documents)} policy document(s)"
        )

        return documents

    def preview_documents(
        self,
        documents: List[Document],
        preview_length: int = 500
    ) -> None:
        """
        Print sample content for validation.
        """

        for idx, doc in enumerate(documents):

            print("\n" + "=" * 80)
            print(f"Document {idx + 1}")
            print("=" * 80)

            print(
                doc.get_content()[:preview_length]
            )

    def export_text(
        self,
        documents: List[Document],
        output_dir: str
    ) -> None:
        """
        Optional debugging utility.
        Saves extracted content as txt files.
        """

        output_path = Path(output_dir)

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        for idx, doc in enumerate(documents):

            file_name = f"document_{idx+1}.txt"

            with open(
                output_path / file_name,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    doc.get_content()
                )

        print(
            f"\nExported {len(documents)} file(s)"
            f" to {output_dir}"
        )


if __name__ == "__main__":

    ingestion = PolicyDocumentIngestion(
        policy_path="docs/policies"
    )

    documents = ingestion.load_documents()

    ingestion.preview_documents(
        documents
    )

    ingestion.export_text(
        documents,
        output_dir="data/processed"
    )