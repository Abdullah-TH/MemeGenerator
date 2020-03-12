from typing import List
from abc import ABC
from quoteModel import QuoteModel


class IngestorInterface(ABC):

    file_extension = ""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        file_extension_length = len(cls.file_extension)
        file_extension = path[-file_extension_length:].lower()
        return file_extension == cls.file_extension

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
