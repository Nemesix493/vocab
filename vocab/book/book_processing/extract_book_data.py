import mobi
from pathlib import Path

from .parsing import ParsingBook
from .processing import ProcessingWordlist


class ExtractBookData:
    """
    This class manage the extraction of data from a book
    """

    @classmethod
    def extract_data(cls, book_path: Path) -> dict:
        try:
            ext = book_path.suffix[1:]
            extract_method = getattr(
                cls,
                f'extract_from_{ext}'
            )
        except AttributeError:
            raise ValueError(f'{cls.__name__} could not extract data from \'.{ext}\' file')
        return extract_method(book_path)

    @classmethod
    def extract_from_mobi(cls, book_path: Path) -> dict:
        _tempdir = mobi.extract(str(book_path))[0]
        html_file = Path(_tempdir).resolve() / 'mobi7' / 'book.html'
        return cls.extract_from_html(
            html_file,
            possible_title=str(book_path.name[:-len(book_path.suffix)]).split('(')[0][:-1]
        )

    @classmethod
    def extract_from_html(cls, book_path: Path, possible_title: str|None = None) -> dict:
        with open(book_path, 'r', encoding='utf-8') as file:
            book_content = file.read()
            return {
                'occurences': ProcessingWordlist.process_words_occurences(
                    ParsingBook.parse_book_words(book_content)
                ),
                'possible_title': possible_title
                if possible_title is not None
                else str(book_path.name[:-len(book_path.suffix)]).split('(')[0][:-1]
            }
