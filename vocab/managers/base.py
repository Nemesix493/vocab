import abc
from pathlib import Path


class BaseManager(abc.ABC):
    @abc.abstractmethod
    @classmethod
    def get_path(cls, managed_obj) -> Path:
        pass
