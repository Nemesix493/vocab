from bs4 import BeautifulSoup


from ...settings.base import FILTERED_SPECIAL_CHARS


class ParsingBook:
    """
    This class manage the parsing of book paragraphs.
    """

    @classmethod
    def parse_book_words(cls, book_html_content: str) -> list[str]:
        """
        This method transform a book (html) to a list a word
        """
        wordlist = list()
        for paragraph in cls.parsing_html_paragraphs(book_html_content):
            for word in cls.paragraph_to_word_list(paragraph):
                wordlist.append(word)
        return wordlist

    @staticmethod
    def parsing_html_paragraphs(book_html_content: str) -> list[str]:
        """
        This method parse the book paragraphs text to a list of str
        """
        soup = BeautifulSoup(book_html_content, 'lxml')
        return [
            p.text
            for p in soup.find_all('p')
        ]

    @staticmethod
    def remove_special_chars(paragraph: str) -> str:
        """
        This method simply change special chars to a space
        """
        for special_char in FILTERED_SPECIAL_CHARS:
            paragraph = paragraph.replace(special_char, ' ')
        return paragraph
    
    @classmethod
    def paragraph_to_word_list(cls, paragraph: str) -> list[str]:
        """
        This method take a paragrah a return a list of word
        remove the special chars and split the paragraph to make a word list
        filter the potential empty str due to the possible multiple spaces
        """
        word_list = cls.remove_special_chars(paragraph).split(' ')
        return [
            word
            for word in word_list
            # filter empty str
            if word != ''
        ]


    


