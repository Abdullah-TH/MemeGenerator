from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel
from docx import Document
from quoteBuilder import QuoteBuilder


class DocxIngestor(IngestorInterface):

    file_extension = 'docx'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Generate a list of QuoteModel from a docx file, given that
        the quotes text are written in the following format:
        "Quote text" - Author name

        :param path: a string of the docx file system path
        :return: list of QuoteModel instances
        """
        doc = Document(path)
        lines = [p.text for p in doc.paragraphs if p.text != '']
        return QuoteBuilder.parse_quote(lines, '- ', '', '"', '"')
