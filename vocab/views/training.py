from math import log2, floor
from itertools import chain
from random import shuffle

from questionary import prompt

from ..book.book import Book
from ..lang.lang_learning_dict.lang_learning_dict import LangLearningDict
from ..lang.lang import LangEnum
from .base_view import BaseView


class Training(BaseView):
    def __init__(
            self,
            book: Book,
            used_lang: LangEnum = LangEnum.french,
            number_levels: int = 5,
            number_words_per_level: int = 10
        ):
        self.number_levels = number_levels
        self.number_words_per_level = number_words_per_level
        self.book = book
        self.used_lang = used_lang
        self.lang_learning_dict = LangLearningDict.get(self.book.lang)
    
    def get_translation_link(self, word: str):
        return {
            'type': 'print',
            'message': f'https://www.wordreference.com/{self.book.lang.value}{self.used_lang.value}/{word}',
            'when': lambda x: x[word] == 'no'
        }

    def get_template(self, *args, **kwargs):
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
            self.get_translation_link(word)

            ]
            for word in self.get_training_words()
        ]))

    def get_words_sorted_by_level(self):
        words_per_sorted_by_level = {
            level : []
            for level in range(self.number_levels)
        }
        low_levels_full = False  # when True stop the filling of levels except the highest level
        # Fill the levels order by reversed occurency (highest occurenced word first, lowest occurenced word last)
        for word in self.book.occurences_without_proper_nouns.keys():
            # Calculate the words level
            word_level = 0
            if word in self.lang_learning_dict.keys():
                word_score = self.lang_learning_dict[word]
                word_level = floor(log2(word_score)) if word_score >= 1 else 0
            # Sort the words by level
            if word_level < self.number_levels - 1 and not low_levels_full:
                words_per_sorted_by_level[word_level].append(word)
                low_levels_full = all([
                    len(val) >= self.number_words_per_level 
                    for key, val in words_per_sorted_by_level.items()
                    if key != self.number_levels - 1
                ])
            elif word_level >= self.number_levels - 1:
                words_per_sorted_by_level[self.number_levels - 1].append(word)
        return words_per_sorted_by_level

    def get_training_words(self):
        preselected_words = self.get_words_sorted_by_level()
        training_words = {
            level : []
            for level in range(self.number_levels)
        }
        # shuffle the highest level
        # all the words in this level have the same probability to get selected
        shuffle(preselected_words[self.number_levels - 1])
        for i in range(self.number_levels):
            total_words = sum([len(wordlist) for wordlist in training_words.values()])
            word_selected_per_level = round(((self.number_levels * self.number_words_per_level) - total_words)/(self.number_levels - i))
            level = self.number_levels - (i+1)
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

    def __call__(self, *args, **kwargs):
        template = self.get_template()
        training_result = prompt(template)
        for word, result in training_result.items():
            if result == 'yes':
                self.lang_learning_dict.add_learning_point(word)
            elif result == 'add to proper nouns':
                self.book.add_proper_nouns(word)
            else:
                self.lang_learning_dict.reset_learning_point(word)
        self.lang_learning_dict.save()
        self.book.save()