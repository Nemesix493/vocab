from abc import (
    ABC as AbstractClass,
    abstractmethod
)


class BaseSerializer(AbstractClass):
    def __init__(self, obj=None, data=None) -> None:
        self._obj = obj
        self._data = data
    
    @property
    def obj(self):
        if self._obj is None:
            self.gen_obj()
        return self._obj

    @property
    def data(self):
        if self._data is None:
            self.gen_data()
        return self._data
    
    @abstractmethod
    def gen_data(self):
        pass

    @abstractmethod
    def gen_obj(self):
        pass