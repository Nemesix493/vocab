from pathlib import Path

from ..managers import BaseManager
from ..settings import BOOK_DIR
from .book_serializer import BookSerializer


class BookManager(BaseManager):
    
    @staticmethod
    def get_filename(name: str):
        return f'{name}.json'

    @classmethod
    def get_path(cls, *args, **kwargs) -> Path:
        return BOOK_DIR / cls.get_filename(*args, **kwargs)