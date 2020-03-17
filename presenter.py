import os
import random

from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


class Presenter:

    @classmethod
    def generate_meme(
            cls,
            output_path,
            image_path=None,
            body=None,
            author=None
    ):
        """ Generate a meme given an path and a quote """
        img = None
        quote = None

        if image_path is None:
            imgs = cls.__get_images()
            img = random.choice(imgs)
        else:
            img = image_path

        if body is None:
            quotes = cls.__get_quotes()
            quote = random.choice(quotes)
        else:
            if author is None:
                raise Exception('Author Required if Body is Used')
            quote = QuoteModel(author, body)

        meme = MemeEngine(output_path)
        path = meme.make_meme(img, quote.body, quote.author)

        return path

    @classmethod
    def __get_quotes(cls):
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
    def __get_images(cls):
        """ Load images resources to list of paths """

        images_path = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images_path):
            imgs = [os.path.join(root, name) for name in files]

        return imgs
