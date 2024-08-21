from questionary import prompt

from ..book.book import Book
from .select_an_ebook import select_an_ebook
from ..book.book_processing.extract_book_data import ExtractBookData
from ..lang.lang import LangEnum

def get_template(possible_title: str):
    return [
        {
            'type': 'confirm',
            'name': 'possible_title_to_title',
            'message': f'Would you kipp \'{possible_title}\' as title ?',
            'qmark': '',
            'default': True
        },
        {
            'type': 'text',
            'name': 'title',
            'message': f'Write the title of this book : ',
            'qmark': '',
            'when': lambda x: not x['possible_title_to_title']
        },
        {
            'type': 'confirm',
            'name': 'possible_title_to_name',
            'message': f'Would you kipp \'{possible_title}\' as name ?',
            'qmark': '',
            'default': True
        },
        {
            'type': 'text',
            'name': 'name',
            'message': f'Write the name you want for this book : ',
            'qmark': '',
            'when': lambda x: not x['possible_title_to_name']
        },
        {
            'type': 'select',
            'name': 'lang',
            'message': 'Select the lang of this ebook :',
            'choices': [name for name in LangEnum._member_names_],
            'qmark': ''

        }

    ]


def add_an_ebook():
    book_data = ExtractBookData.extract_data(select_an_ebook())
    form = prompt(get_template(book_data['possible_title']))
    new_book = Book(
        **{
            'occurences': book_data['occurences'],
            'lang': LangEnum._member_map_[form['lang']],
            'name': book_data['possible_title'] if form['possible_title_to_name'] else form['name'],
            'title': book_data['possible_title'] if form['possible_title_to_title'] else form['title']
        }
    )
    new_book.save()
