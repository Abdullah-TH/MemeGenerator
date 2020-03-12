import pandas
from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel


class CSVIngestor(IngestorInterface):

    file_extension = 'csv'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        result = []
        with open(path) as file:
            data = pandas.read_csv(file)
            for i in range(len(data)):
                result.append(QuoteModel(data.get('author')[i], data.get('body')[i]))

        return result
