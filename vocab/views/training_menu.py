from questionary import prompt

from .training import training
from .base_view import BaseView
from ..book.book import Book


class TrainingMenu(BaseView):
    def get_template(self, *args, **kwargs):
        book_list = Book.manager_class.book_list()
        return [
            {
                'type': 'print',
                'message': '\nTraining !',
                'style': 'fg:#ffffff bold'
            },
            {
                'type': 'select',
                'name': 'book_name',
                'message': "With which book would you like to learn ?",
                'choices': book_list,
                'qmark': ''
            },
            {
                'type': 'print',
                'message': '',
            }
        ]
    
    def __call__(self, *args, **kwargs):
        training(
            Book.get(prompt(self.get_template())['book_name'])
        )