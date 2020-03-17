import subprocess

from typing import List
from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel
from .textIngestor import TextIngestor


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']
    txt_file_path = '_data/DogQuotes/DogQuotesPDF.txt'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Generate a list of QuoteModel from a PDF file, given that
        the quotes text are written in the following format:
        "Quote text" - Author name

        :param path: a string of the pdf file system path
        :return: list of QuoteModel instances
        """
        super().parse(path)
        command = r'{} "{}" "{}" -enc UTF-8' \
            .format('pdftotext', path, cls.txt_file_path)
        try:
            subprocess.call(command, shell=True, stderr=subprocess.STDOUT)
            cls.__clean_txt_file()
            return TextIngestor.parse(cls.txt_file_path)
        except Exception as e:
            print(
                str(e),
                'Command "pdftotext" not found, please install it first'
            )

    @classmethod
    def __clean_txt_file(cls):
        """
        Helper function called by the class function parse
        this method clean a text file by removing blank lines
        and quotation marks
        """
        new_lines = []
        with open(cls.txt_file_path) as file:
            lines = file.readlines()
            new_lines = [line.replace('"', '') for line in lines
                         if not line.isspace()]

        with open(cls.txt_file_path, 'w') as file:
            file.writelines(new_lines)
