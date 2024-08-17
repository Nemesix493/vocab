from pathlib import Path

from ...managers.base import BaseManager
from .lang_learning_dict_serializer import LangLearningDictSerializer
from ...settings import LANG_LEARNING_DICT_DIR
from ..lang import LangEnum


class LangLearningDictManager(BaseManager):

    __serializer_class__ = LangLearningDictSerializer
    
    @staticmethod
    def get_filename(lang: LangEnum):
        return f'{lang}.json'

    @classmethod
    def get_path(cls, *args, **kwargs) -> Path:
        return LANG_LEARNING_DICT_DIR / cls.get_filename(*args, **kwargs)
