import random

from argparse import ArgumentParser
from presenter import Presenter

# @TODO Import your Ingestor and MemeEngine classes
# presenter.py uses the Ingestor, and this file use the Presenter
from MemeEngine import MemeEngine
from QuoteEngine import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        imgs = Presenter.get_images()
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quotes = Presenter.get_quotes()
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(author, body)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = ArgumentParser(description="Generate memes!")
    parser.add_argument('--path', type=str, help='Path to an image file')
    parser.add_argument('--body', type=str, help='Quote body to add to the image')
    parser.add_argument('--author', type=str, help='Quote author to add to the image')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
