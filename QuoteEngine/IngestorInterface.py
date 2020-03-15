from typing import List
from abc import ABC, abstractmethod
from quoteModel import QuoteModel


class IngestorInterface(ABC):

    file_extension = ""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determine if the file type can be ingested (parsed)

        :param path: a string of the file system path
        :return: True if the file can be parsed, False otherwise
        """
        file_extension_length = len(cls.file_extension)
        file_extension = path[-file_extension_length:].lower()
        return file_extension == cls.file_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest file {path}')
