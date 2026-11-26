
"""
NovaMind - Document Reader
Extracts text from PDF and TXT documents.
"""

from pathlib import Path
from pypdf import PdfReader


class DocumentReader:

    @staticmethod
    def read_pdf(file_path: str) -> str:
        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages.append(text)

        return "\n".join(pages)

    @staticmethod
    def read_txt(file_path: str) -> str:
        return Path(file_path).read_text(
            encoding="utf-8"
        )
