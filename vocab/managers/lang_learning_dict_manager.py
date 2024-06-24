from pathlib import Path

from .base import BaseManager
from ..serializers import LangLearningDictSerializer
from ..settings import LANG_LEARNING_DICT_DIR
from ..lang.lang import LangEnum


class LangLearningDictManager(BaseManager):

    serializer_class = LangLearningDictSerializer
    
    @staticmethod
    def get_filename(lang: LangEnum):
        return f'{lang}.json'

    @classmethod
    def get_path(cls, *args, **kwargs) -> Path:
        return LANG_LEARNING_DICT_DIR / cls.get_filename(*args, **kwargs)
