from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel
from pdfminer import high_level as pdf


class PDFIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        file_extension = path[-3:].lower()
        return file_extension == "pdf"

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        result = []
        with open(path, 'rb') as file:
            text = pdf.extract_text(path).strip().split("\n")
            for line in text:
                body = cls.__parse_line(line, '"', '"')
                author = cls.__parse_line(line, "- ", "")
                quote = QuoteModel(author, body)
                result.append(quote)

        return result

    @classmethod
    def __parse_line(cls, string, start, end):
        return string[string.find(start) + len(start):string.rfind(end)]
