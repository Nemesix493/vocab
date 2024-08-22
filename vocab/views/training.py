from math import log2, floor
from itertools import chain
from random import shuffle

from questionary import prompt

from ..book.book import Book
from ..lang.lang_learning_dict.lang_learning_dict import LangLearningDict
from ..lang.lang import LangEnum


def get_translation_link(word: str, lang_in: LangEnum, lang_out: LangEnum = LangEnum.french):
    return {
        'type': 'print',
        'message': f'https://www.wordreference.com/{lang_in.value}{lang_out.value}/{word}',
        'when': lambda x: x[word] == 'no'
    }


def get_template(book: Book, lang_learning_dict: LangLearningDict):
    return list(chain(*[
        [
        {
            'type': 'select',
            'name': word,
            'message': f'Do you know this word \'{word}\' ?',
            'choices': ['no', 'yes', 'add to proper nouns'],
            'default': 'yes',
            'qmark': ''
        },
        get_translation_link(word, book.lang)

        ]
        for word in get_training_words(book, lang_learning_dict)
    ]))


def get_words_sorted_by_level(
        book: Book,
        lang_learning_dict: LangLearningDict,
        number_levels: int = 5,
        number_words_per_level: int = 10
    ):
    words_per_sorted_by_level = {
        level : []
        for level in range(number_levels)
    }
    low_levels_full = False  # when True stop the filling of levels except the highest level
    # Fill the levels order by reversed occurency (highest occurenced word first, lowest occurenced word last)
    for word in book.occurences_without_proper_nouns.keys():
        # Calculate the words level
        word_level = 0
        if word in lang_learning_dict.keys():
            word_score = lang_learning_dict[word]
            word_level = floor(log2(word_score)) if word_score >= 1 else 0
        # Sort the words by level
        if word_level < number_levels - 1 and not low_levels_full:
            words_per_sorted_by_level[word_level].append(word)
            low_levels_full = all([
                len(val) >= number_words_per_level 
                for key, val in words_per_sorted_by_level.items()
                if key != number_levels - 1
            ])
        else:
            words_per_sorted_by_level[number_levels - 1].append(word)
    return words_per_sorted_by_level


def get_training_words(book: Book, lang_learning_dict: LangLearningDict):
    levels = 5
    word_per_level = 10
    preselected_words = get_words_sorted_by_level(book, lang_learning_dict)
    training_words = {
        level : []
        for level in range(levels)
    }
    # shuffle the highest level
    # all the words in this level have the same probability to get selected
    shuffle(preselected_words[levels - 1])
    for i in range(levels):
        total_words = sum([len(wordlist) for wordlist in training_words.values()])
        word_selected_per_level = round(((levels * word_per_level) - total_words)/(levels - i))
        level = levels - (i+1)
        if len(preselected_words[level]) < word_selected_per_level:
            training_words[level] = preselected_words[level]
        else:
            training_words[level] = preselected_words[level][:word_selected_per_level]
    return list(chain(
        *[
            words
            for words in training_words.values()
        ]
    ))

def training(book: Book):
    lang_learning_dict = LangLearningDict.get(book.lang)
    template = get_template(book, lang_learning_dict)
    training_result = prompt(template)
    for word, result in training_result.items():
        if result == 'yes':
            lang_learning_dict.add_learning_point(word)
        elif result == 'add to proper nouns':
            book.add_proper_nouns(word)
        else:
            lang_learning_dict.reset_learning_point(word)
    lang_learning_dict.save()
    book.save()