import re
from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel
from docx import Document


class DOCIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        file_extension = path[-4:].lower()
        return file_extension == "docx"

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        result = []
        doc = Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text == "":
                continue
            body = cls.__parse_line(paragraph.text, '"', '"')
            author = cls.__parse_line(paragraph.text, "- ", "")
            result.append(QuoteModel(author, body))

    @classmethod
    def __parse_line(cls, string, start, end):
        return string[string.find(start) + len(start):string.rfind(end)]
