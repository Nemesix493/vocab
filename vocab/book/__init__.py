from .book import Book

from .book_serializer import BookSerializer
from .book_manager import BookManager

BookSerializer.__model_class__ = Book
BookManager.__serializer_class__ = BookSerializer
Book.manager_class = BookManager