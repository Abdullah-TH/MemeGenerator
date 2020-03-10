from typing import List
from abc import ABC
from quoteModel import QuoteModel


class IngestorInterface(ABC):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        pass

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
