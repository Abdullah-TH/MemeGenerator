from typing import List
from abc import ABC, abstractmethod
from .quoteModel import QuoteModel


class IngestorInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determine if the file type can be ingested (parsed)

        :param path: a string of the file system path
        :return: True if the file can be parsed, False otherwise
        """
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest file {path}')
