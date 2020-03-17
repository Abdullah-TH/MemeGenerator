from typing import List
from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel
from .csvIngestor import CSVIngestor
from .docxIngestor import DocxIngestor
from .pdfIngestor import PDFIngestor
from .textIngestor import TextIngestor


class Ingestor(IngestorInterface):

    allowed_extensions = ['csv', 'docx', 'pdf', 'txt']
    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Generate a list of QuoteModel from a supported file,
        if the file type is not supported, an exception will be
        thrown

        :param path: a string of the file system path
        :return: list of QuoteModel instances
        """
        super().raise_error_if_cannot_ingest(path)

        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise Exception(f'Cannot ingest file {path}')
