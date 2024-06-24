from abc import (
    ABC,
    abstractmethod
)
from json import (
    dump as json_dump,
    load as json_load
)
from pathlib import Path


class BaseManager(ABC):

    serializer_class = None

    @classmethod
    @abstractmethod
    def get_path(cls, *args, **kwargs) -> Path:
        pass

    @classmethod
    def save(cls, managed_obj) -> None:
        with open(cls.get_path(managed_obj.__lang__), 'w', encoding='utf-8') as save_file:
            json_dump(
                cls.serializer_class(obj=managed_obj).data,
                save_file
            )
    
    @classmethod
    def load(cls, *args, **kwargs):
        with open(cls.get_path(*args, **kwargs), 'r', encoding='utf-8') as load_file:
            return cls.serializer_class(data=json_load(load_file))

