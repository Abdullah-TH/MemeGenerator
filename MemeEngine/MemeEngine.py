from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class MemeEngine:

    def __init__(self, path):
        self.path = path

    def make_meme(self, img_path, text, author, width=500):
        if width > 500:
            raise Exception('width should be at most 500px')

        img = Image.open(self.path)
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        img_draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/01211_AHDSANSB.ttf', size=20)
        img_draw.text((10, 30), f'{text} - {author}', font=font, fill='white')

        output_path = './meme.jpg'
        img.save(output_path)
        return output_path
