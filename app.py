import random
import os
import requests

from presenter import Presenter
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
# imported in Presenter

app = Flask(__name__)


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    path = Presenter.generate_meme('./static')
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form.get('image_url')
    author = request.form.get('author')
    body = request.form.get('body')

    response = requests.get(image_url, allow_redirects=True)
    tmp = f'./tmp/{random.randint(0, 100000000)}.png'
    open(tmp, 'wb').write(response.content)

    path = meme.make_meme(tmp, body, author)

    os.remove(tmp)
    print('path: ' + path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
