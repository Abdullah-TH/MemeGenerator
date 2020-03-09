class QuoteModel:

    def __init__(self, author: str, body: str):
        self.author = author
        self.body = body

    def __str__(self):
        return f"Author: {self.author}, Body: {self.body}"
