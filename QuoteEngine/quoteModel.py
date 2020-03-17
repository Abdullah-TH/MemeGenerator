class QuoteModel:
    """
    A class that represents Quote with author and body (the actual quote)

    Attributes:
        author (str): A string.
        body (str): A string.

    """

    def __init__(self, author: str, body: str):
        self.author = author
        self.body = body

    def __repr__(self):
        return f'"{self.body}" - {self.author}'
