from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel
from csvIngestor import CSVIngestor
from docxIngestor import DocxIngestor
from pdfIngestor import PDFIngestor
from textIngestor import TextIngestor


class Ingestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determine if the file type can be ingested (parsed)

        :param path: a string of the file system path
        :return: True if the file can be parsed, False otherwise
        """
        return CSVIngestor.can_ingest(path) or \
               DocxIngestor.can_ingest(path) or \
               PDFIngestor.can_ingest(path) or \
               TextIngestor.can_ingest(path)

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Generate a list of QuoteModel from a supported file,
        if the file type is not supported, an exception will be
        thrown

        :param path: a string of the file system path
        :return: list of QuoteModel instances
        """
        if path[-3:].lower() == 'csv':
            return CSVIngestor.parse(path)
        elif path[-4:].lower() == 'docx':
            return DocxIngestor.parse(path)
        elif path[-3:].lower() == 'pdf':
            return PDFIngestor.parse(path)
        elif path[-3:].lower() == 'txt':
            return TextIngestor.parse(path)
        else:
            raise Exception('File type is not supported')
