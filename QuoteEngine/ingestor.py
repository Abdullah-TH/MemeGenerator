from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel
from csvIngestor import CSVIngestor
from docIngestor import DOCIngestor
from pdfIngestor import PDFIngestor
from textIngestor import TextIngestor


class Ingestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return CSVIngestor.can_ingest(path) or \
               DOCIngestor.can_ingest(path) or \
               PDFIngestor.can_ingest(path) or \
               TextIngestor.can_ingest(path)

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if path[-3:].lower() == 'csv':
            return CSVIngestor.parse(path)
        elif path[-4:].lower() == 'docx':
            return DOCIngestor.parse(path)
        elif path[-3:].lower() == 'pdf':
            return PDFIngestor.parse(path)
        elif path[-3:].lower() == 'txt':
            return TextIngestor.parse(path)
        else:
            raise Exception('File type is not supported')
