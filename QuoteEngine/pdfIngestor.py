import subprocess

from typing import List
from ingestorInterface import IngestorInterface
from quoteModel import QuoteModel
from textIngestor import TextIngestor


class PDFIngestor(IngestorInterface):

    file_extension = 'pdf'
    txt_file_path = '_data/DogQuotes/DogQuotesPDF.txt'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        command = r'{} "{}" "{}" -enc UTF-8'.format('pdftotext', path, cls.txt_file_path)
        subprocess.call(command, shell=True, stderr=subprocess.STDOUT)
        cls.__clean_txt_file()
        return TextIngestor.parse(cls.txt_file_path)

    @classmethod
    def __clean_txt_file(cls):
        new_lines = []
        with open(cls.txt_file_path) as file:
            lines = file.readlines()
            new_lines = [line.replace('"', '') for line in lines if not line.isspace()]

        with open(cls.txt_file_path, 'w') as file:
            file.writelines(new_lines)
