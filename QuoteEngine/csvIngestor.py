import csv
from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel


class CSVIngestor(IngestorInterface):

    file_extension = 'csv'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        result = []
        with open(path) as file:
            reader = csv.reader(file)
            first_row = True
            for row in reader:
                if first_row:
                    first_row = False
                    continue
                quote = QuoteModel(row[1], row[0])
                result.append(quote)
        return result
