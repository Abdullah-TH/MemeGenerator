from argparse import ArgumentParser
from presenter import Presenter

# @TODO Import your Ingestor and MemeEngine classes
# imported in Presenter


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
    print(Presenter.generate_meme('./tmp', args.path, args.body, args.author))
