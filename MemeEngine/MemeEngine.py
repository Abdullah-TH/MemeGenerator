from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import randrange


class MemeEngine:

    def __init__(self, path):
        self.output_path = path

    def make_meme(self, img_path, text, author, width=500):
        """
        Generate a meme image with overlaying text and author

        :param img_path: a path of the image you want to apply the text on
        :param text: a string that will be drawn on the image as the body of the quote
        :param author: a string that will be drawn on the image as the author of the quote
        :param width: an int represent the width of the generated image in pixels (default 500px)
        :param author:

        :return: list of QuoteModel instances
        """

        if width > 500:
            raise Exception('width should be at most 500px')

        try:
            img = Image.open(img_path)
        except FileNotFoundError:
            print(f'File not found on path: {img_path}')
            return

        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        img_draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype('./fonts/01211_AHDSANSB.ttf', size=20)
        except OSError:
            print("The file /fonts/01211_AHDSANSB.ttf is missing")
            return

        random_x = randrange(width / 2)
        random_y = randrange(height - 30)
        img_draw.text((random_x, random_y), f'{text} - {author}', font=font, fill='white')

        try:
            img.save(self.output_path)
        except ValueError as error:
            print(error)
            return

        return self.output_path
