from abc import (
    ABC as AbstractClass,
    abstractmethod
)


class BaseSerializer(AbstractClass):
    def __init__(self, obj=None) -> None:
        self.obj = obj
    
    @abstractmethod
    @property
    def data(self):
        pass