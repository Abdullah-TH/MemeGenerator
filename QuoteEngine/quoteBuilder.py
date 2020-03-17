from .quoteModel import QuoteModel


class QuoteBuilder:

    @classmethod
    def parse_quote(
            cls,
            quotes,
            author_start,
            author_end,
            body_start,
            body_end
    ):
        """
        Given a list of strings, parse each string to a QuoteModel object.
        Each QuoteModel object needs an author string and body string.
        This method tries to extract these information from the strings
        using delimiters.
        You specify the two delimiters that surround the author string
        and the two delimiters that surround the body string.

        :param quotes: list of strings
        :param author_start: the start delimiter for author
        :param author_end: the end delimiter for author
        :param body_start: the start delimiter for body
        :param body_end: the end delimiter for body
        :return: list of QuoteModel instances
        """
        result = []
        for quote in quotes:
            author = cls.__parse_line(quote, author_start, author_end)
            body = cls.__parse_line(quote, body_start, body_end)
            quote_model = QuoteModel(author, body)
            result.append(quote_model)
        return result

    @classmethod
    def __parse_line(cls, string, start, end):
        """
        Given a string and two delimiters, return the string
        occurring between those two delimiters.

        :param string: string that contain that contain the two delimiters
        :param start: the first delimiters
        :param end: the second delimiters
        :return: string occurring between start and end
        """
        return string[string.find(start) + len(start):string.rfind(end)]
