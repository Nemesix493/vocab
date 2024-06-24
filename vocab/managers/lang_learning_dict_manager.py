from pathlib import Path

from .base import BaseManager
from ..serializers import LangLearningDictSerializer
from ..settings import DATA_DIR
from ..lang.lang import LangEnum


BASE_LANG_DICT_DIR = DATA_DIR / 'lang_learning_dict'


class LangLearningDictManager(BaseManager):

    serializer_class = LangLearningDictSerializer
    
    @staticmethod
    def get_filename(lang: LangEnum):
        return f'{lang}.json'

    @classmethod
    def get_path(cls, *args, **kwargs) -> Path:
        return BASE_LANG_DICT_DIR / cls.get_filename(*args, **kwargs)
