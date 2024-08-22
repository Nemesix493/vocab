from collections import OrderedDict

from ..lang.lang import LangEnum


class Book:

    manager_class = None

    def __init__(self, **kwargs):
        self._proper_nouns = []
        self._occurences = OrderedDict()
        for key, val in kwargs.items():
            self.__setattr__(key, val)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError('name should be a String')
        self._name = value

    @property
    def id(self):
        return self._name
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value: str):
        if not isinstance(value, str):
            raise ValueError('title should be a String')
        self._title = value
    
    @property
    def lang(self):
        return self._lang
    
    @lang.setter
    def lang(self, value: LangEnum):
        if not isinstance(value, LangEnum):
            raise ValueError('lang should be a LangEnum Object')
        self._lang = value
    
    @property
    def proper_nouns(self):
        return self._proper_nouns
    
    @proper_nouns.setter
    def proper_nouns(self, value: list[str]):
        if isinstance(value, list):
            if all(isinstance(val, str) for val in value):
                self._proper_nouns = value
                return None
        raise ValueError('proper_nouns should be a list of String')
    
    def add_proper_nouns(self, value: str):
        if not isinstance(value, str):
            raise ValueError('proper noun should be a String')
        self._proper_nouns.append(value)

    @property
    def occurences(self) -> OrderedDict:
        return self._occurences
    
    @occurences.setter
    def occurences(self, value: dict[str:int]):
        if isinstance(value, dict):
            if all(isinstance(key, str) and isinstance(val, int) for key, val in value.items()):
                self._occurences = OrderedDict(sorted(
                    value.items(),
                    key=lambda item: item[1],
                    reverse=True
                ))
                return None
        raise ValueError('occurences should be a dict with key is a str and value is an int')

    @property
    def word_list(self) -> list[str]:
        return self._occurences.keys()
    
    @property
    def occurences_without_proper_nouns(self) -> OrderedDict:
        return OrderedDict(sorted(
            [
                item
                for item in self._occurences.items()
                if item[0] not in self._proper_nouns
            ],
            key=lambda item: item[1],
            reverse=True
        ))
    
    def save(self):
        self.manager_class.save(self)

    @classmethod
    def get(cls, name: str):
        return cls.manager_class.load(name)
