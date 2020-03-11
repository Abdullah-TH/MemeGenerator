class QuoteModel:

    def __init__(self, author: str, body: str):
        self.author = author
        self.body = body

    def __repr__(self):
        return f"Author: {self.author}, Body: {self.body}"
