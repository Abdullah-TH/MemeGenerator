from quoteModel import QuoteModel


class QuoteBuilder:

    @classmethod
    def parse_quote(cls, quotes, author_start, author_end, body_start, body_end):
        result = []
        for quote in quotes:
            author = cls.__parse_line(quote, author_start, author_end)
            body = cls.__parse_line(quote, body_start, body_end)
            quote_model = QuoteModel(author, body)
            result.append(quote_model)
        return result

    @classmethod
    def __parse_line(cls, string, start, end):
        return string[string.find(start) + len(start):string.rfind(end)]
