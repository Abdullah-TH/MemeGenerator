from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel
from docx import Document
from quoteBuilder import QuoteBuilder


class DOCIngestor(IngestorInterface):

    file_extension = 'docx'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        doc = Document(path)
        lines = [p.text for p in doc.paragraphs if p.text != '']
        return QuoteBuilder.parse_quote(lines, '- ', '', '"', '"')
