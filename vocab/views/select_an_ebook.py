from pathlib import Path
import os

from questionary import prompt

from ..settings.base import BASE_EBOOK_DIR



os.chdir(BASE_EBOOK_DIR)

supported_ebook_type = ['.html', '.mobi']

def path_filter(path):
    path_path = BASE_EBOOK_DIR.joinpath(path)
    if  path_path.is_file() and path_path.suffix not in supported_ebook_type:
        return False
    return True

def path_validator(path):
    path_path = BASE_EBOOK_DIR.joinpath(path)
    if  path_path.is_file() and path_path.suffix in supported_ebook_type:
        return True
    return False


def get_template():
    return [
        {
            'type': 'path',
            'name': 'ebook_path',
            'message': 'Choose your ebook :',
            'qmark': '',
            'file_filter': path_filter,
            'validate': path_validator
        }
    ]

def select_an_ebook():
    return BASE_EBOOK_DIR.joinpath(prompt(get_template())['ebook_path'])