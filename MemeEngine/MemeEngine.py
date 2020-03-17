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

        img = self.__load_image(img_path)
        img = self.__resize_image(img, width)
        self.__add_caption(img, width, text, author)
        output_image_path = self.__save_image(img_path, img)
        return output_image_path

    def __load_image(self, path):
        """Load Image from path"""
        return Image.open(path)

    def __resize_image(self, image, width):
        """
        Resize an image using the specified width
        and adjust the height automatically to keep the same
        image's ration

        :param image: the Image you want to resize
        :param width: width of the image in pixels
        :return: the new resized Image
        """
        ratio = width / float(image.size[0])
        height = int(ratio * float(image.size[1]))
        img = image.resize((width, height), Image.NEAREST)
        return img

    def __add_caption(self, image, width, text, author):
        """
        Add text and author on the image at random location
        The method draw on the same passed image parameter

        :param image: the Image you want to draw text and author on
        :param width: width in pixels used to put the texts at
        appropriate location
        :param text: body text to draw on image
        :param author: author text to draw on image
        """
        img_draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('./fonts/01211_AHDSANSB.ttf', size=20)
        random_x = randrange(width // 3)
        random_y = randrange(width // 2)
        img_draw.text((random_x, random_y),
                      f'{text} \n- {author}',
                      font=font,
                      fill='white',
                      stroke_width=1,
                      stroke_fill='black')

    def __save_image(self, image_path, image):
        """
        Save the image on self.output_path using the same
        extension from parameter image_path
        :param image_path: the image path you want to save
        :param image: the image you want to save
        :return: path of the saved image
        """
        img_extension = image_path.split('.')[-1]
        output_image_path = self.output_path \
            + f'/meme{randrange(1000)}.{img_extension}'
        image.save(output_image_path)
        return output_image_path
