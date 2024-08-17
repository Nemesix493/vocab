from unittest import TestCase

from .. import Book
from ...lang import LangEnum

class TestsBookSave(TestCase):
    def test(self):
        print('book')
        try:
            book_test = Book(
                **{
                    'title': 'test',
                    'name': 'test_name',
                    'occurences': {
                        'clear': 10,
                        'blue': 5
                    },
                    'proper_nouns': [],
                    'lang': LangEnum.english
                }
            )
            book_test.save()
            loaded_book = Book.get(name='test_name')
            data = Book.manager_class.serializer_class(obj=loaded_book).data
            self.assertEqual(
                data,
                {
                    'title': 'test',
                    'name': 'test_name',
                    'occurences': {
                        'clear': 10,
                        'blue': 5
                    },
                    'proper_nouns': [],
                    'lang': LangEnum.english.value
                }
            )
            
        except:
            self.assertFalse(True)
