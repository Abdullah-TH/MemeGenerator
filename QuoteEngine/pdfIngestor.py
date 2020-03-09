from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel


class PDFIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        pass

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        pass
