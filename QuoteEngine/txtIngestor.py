from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel
from quoteBuilder import QuoteBuilder


class TXTIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        file_extension = path[-3:].lower()
        return file_extension == "txt"

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        with open(path, encoding='utf-8-sig') as file:
            lines = file.read().splitlines()
            return QuoteBuilder.parse_quote(lines, "- ", "", "", " -")
