import pandas
from typing import List
from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel


class CSVIngestor(IngestorInterface):

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Generate a list of QuoteModel from a csv file, given that
        the csv file is structured as 2 columns with headings of author
        and body respectively

        :param path: a string of the csv file system path
        :return: list of QuoteModel instances
        """
        super().parse(path)
        result = []
        with open(path) as file:
            data = pandas.read_csv(file)
            for i in range(len(data)):
                result.append(QuoteModel(data.get('author')[i], data.get('body')[i]))

        return result
