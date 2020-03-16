import os

from QuoteEngine import Ingestor


class Presenter:

    @classmethod
    def get_quotes(cls):
        """ Load quotes resources to list """

        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))

        return quotes

    @classmethod
    def get_images(cls):
        """ Load images resources to list of paths """

        images_path = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images_path):
            imgs = [os.path.join(root, name) for name in files]

        return imgs
