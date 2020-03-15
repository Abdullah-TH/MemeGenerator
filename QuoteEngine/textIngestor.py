from typing import List
from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel
from .quoteBuilder import QuoteBuilder


class TextIngestor(IngestorInterface):

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Generate a list of QuoteModel from a txt file, given that
        the quotes text are written in the following format:
        Quote text - Author name

        :param path: a string of the txt file system path
        :return: list of QuoteModel instances
        """
        super().parse(path)
        with open(path, encoding='utf-8-sig') as file:
            lines = file.read().splitlines()
            return QuoteBuilder.parse_quote(lines, "- ", "", "", " -")
