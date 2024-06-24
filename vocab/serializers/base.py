from abc import (
    ABC as AbstractClass,
    abstractmethod
)


class BaseSerializer(AbstractClass):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    @abstractmethod
    def data(self):
        pass