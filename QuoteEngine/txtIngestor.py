from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel


class TXTIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        pass

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        pass