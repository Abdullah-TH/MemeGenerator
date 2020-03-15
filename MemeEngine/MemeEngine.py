from PIL import Image


class MemeEngine:

    def __init__(self, path):
        self.path = path

    def load_image(self):
        img = Image.open(self.path)
        return img

    def make_meme(self, img_path, text, author, width=500):


meme = MemeEngine('_data/photos/dog/xander_1.jpg')
print(meme.load_image())
