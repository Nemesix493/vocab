from pathlib import Path
import os

from ..managers import BaseManager
from ..settings import BOOK_DIR
from .book_serializer import BookSerializer


class BookManager(BaseManager):

    @staticmethod
    def book_list():
        return [file[:-5] for file in os.listdir(BOOK_DIR) if file.endswith('.json')]
    
    @staticmethod
    def get_filename(name: str):
        return f'{name}.json'

    @classmethod
    def get_path(cls, *args, **kwargs) -> Path:
        return BOOK_DIR / cls.get_filename(*args, **kwargs)