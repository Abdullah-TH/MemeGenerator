from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel
from pdfminer import high_level as pdf
from quoteBuilder import QuoteBuilder


class PDFIngestor(IngestorInterface):

    file_extension = 'pdf'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        with open(path, 'rb') as file:
            lines = pdf.extract_text(path).strip().split("\n")
            return QuoteBuilder.parse_quote(lines, "- ", "", '"', '"')
