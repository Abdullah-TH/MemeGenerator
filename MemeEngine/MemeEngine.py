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
        :param text: a string that will be drawn on the image
        as the body of the quote
        :param author: a string that will be drawn on the image
         as the author of the quote
        :param width: an int represent the width of the
        generated image in pixels (default 500px)

        :return: list of QuoteModel instances

        :raise ValueError: if width > 500
        :raise FileNotFoundError: if img_path is not found
        :raise OSError: if font file at "./fonts/01211_AHDSANSB.ttf" is missing
        :raise ValueError: if MemeEngine.output_path is invalid
        """

        if width > 500:
            raise ValueError('width should be at most 500px')

        img_extension = img_path.split('.')[-1]
        img = Image.open(img_path)

        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        img_draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/01211_AHDSANSB.ttf', size=20)
        random_x = randrange(width / 2)
        random_y = randrange(height - 30)
        img_draw.text((random_x, random_y),
                      f'{text} \n- {author}',
                      font=font,
                      fill='white',
                      stroke_width=1,
                      stroke_fill='black')

        output_image_path = self.output_path \
            + f'/meme{randrange(1000)}.{img_extension}'
        img.save(output_image_path)
        return output_image_path
