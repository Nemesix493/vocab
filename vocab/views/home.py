from questionary import prompt

from .add_an_ebook import add_an_ebook
from .training_menu import TrainingMenu


options = {
    'Start to learn': TrainingMenu(),
    'Add an ebook': add_an_ebook,
    'Quit': quit
}

template = [
    {
        'type': 'print',
        'message': 'Home',
        'style': 'fg:#ffffff bold'
    },
    {
        'type': 'select',
        'name': 'option',
        'message': "What do you want to do?",
        'choices': options.keys(),
        'qmark': ''
    },
    {
        'type': 'print',
        'message': '',
    }
]

def home():
    while True:
        options[prompt(template)['option']]()