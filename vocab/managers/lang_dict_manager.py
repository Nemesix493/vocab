from .base import BaseManager
from pathlib import Path

BASE_LANG_DICT_DIR = Path(__file__).resolve().parent.parent.parent / 'dict'


class LangDictManager(BaseManager):
    @classmethod
    def get_path(cls, managed_obj) -> Path:
        return BASE_LANG_DICT_DIR / f'{managed_obj.lang}.json'
