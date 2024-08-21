from questionary import prompt


options = {
    'Start to learn': lambda : print('Start to learn'),
    'Add an ebook': lambda : print('Add an ebook'),
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