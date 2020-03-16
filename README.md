#Meme Generator
A command line tool and a web site (run locally) to generates memes images.

## Install
download or clone the project to your computer.

## Using the Generator
There are two ways to generate memes, one with CLI tool and one with a local website runs on your machine.

### Command Line Tool
Navigate to the project root folder in your terminal then run:
`python3 meme.py`
This will generate a random image with random text and random author.
To use your own image, text and author you can specify arguments to the program like:
```
python --path "Your_image_path" --body "Your_body_text --author "name_of_author"
```

All parameters are optional, if one is not specified, a random when will be generated.

```
optional arguments:
  -h, --help       show this help message and exit
  --path PATH      Path to an image file
  --body BODY      Quote body to add to the image
  --author AUTHOR  Quote author to add to the image
```

All generated images from this tool will be stored on the `./tmp` directory.

### Local Website
To use a local website with GUI interface, you can run:
`python3 app.py`
You will get an output in your terminal with a URL like this:
` Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
`
copy and past the URL to your browser to start using the web tool.

All generated images from this website will be stored on the `./static` directory.

## Modules Overview
There are two modules within this project `QuoteEngine` and `MemeEngine`

### QuoteEngine
There are many classes in this module, most of them are helpers class.
The main ones you can use in your project are `Ingestor` class and `QuoteModel`
The `Ingestor` class can parse files that contain quotes in the following format:
`"body text" - author_name`
The supported file that can be used by the `Ingestor` class are `csv`, `docx`, `pdf` and `txt`
The `Ingestor`'s `parse(path)` method return a list of `QuoteModel`s
Usage is as follow:
```python
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel

quotes = Ingestor.parse('path_to_your_file')
for quote in quotes:
    print(quote.body)
    print(quote.author)
```

`quotes` in this example will contain a list of `QuoteModel` instances.
You can get the quote's text and quote's author from `QuoteModel` instance using the instance variables `body` and `author`

If the file type is not supported or not formatted properly, an exception will be thrown of type `ValueError`

### MemeEngine

The MemeEngine module contain only one class with the same name `MemeEngine`
This class uses the Pillow library to generate images.
Usage is as follow:
```python
from MemeEngine import MemeEngine

meme = MemeEngine('output_directory')
result_image_path = meme.make_meme('input_image_path', 'quote body text', 'quote author')
```

