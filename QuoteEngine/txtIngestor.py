from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel


class TXTIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        file_extension = path[-3:].lower()
        return file_extension == "txt"

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        result = []
        with open(path, encoding='utf-8-sig') as file:
            lines = file.read().splitlines()
            for line in lines:
                body = cls.__parse_line(line, '', ' -')
                author = cls.__parse_line(line, "- ", "")
                quote = QuoteModel(author, body)
                result.append(quote)
        return result

    @classmethod
    def __parse_line(cls, string, start, end):
        return string[string.find(start) + len(start):string.rfind(end)]
