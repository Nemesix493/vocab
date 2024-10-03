from questionary import prompt

template = [
    {
        'type': 'print',
        'message': '\nWelcome in VOCAB !',
        'style': 'fg:#ffffff bold'
    },
    {
        'type': 'print',
        'message': 'Vocab is tool to learn vocabulary with ebook and step up in foreign languages !\n',
        'style': 'fg:#ffffff'
    }

]

def intro():
    prompt(template)
    