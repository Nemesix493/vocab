from .lang import LangEnum


class LangLearningDict(dict):

    __instances__ = []

    manager_class = None

    def __init__(self, __lang__: LangEnum, *args, **kwargs):
        instance = self.does_instance_exist(__lang__)
        if instance is not None:
            self = instance
        else:
            self.__lang__ = __lang__
            super().__init__(self, *args, **kwargs)
            self.__instances__.append(self)
    
    @property
    def id(self):
        return self.__lang__

    def add_learning_point(self, key: str) -> None:
        if key in self.keys():
            self[key] += 1
        else:
            self[key] = 1

    def reset_learning_point(self, key: str) -> None:
        self[key] = 0

    def save(self):
        self.manager_class.save(self)
    
    @classmethod
    def get(cls, __lang__: LangEnum):
        instance = cls.does_instance_exist(__lang__)
        if instance is not None:
            return instance
        try:
            return cls.manager_class.load(__lang__)
        except FileNotFoundError:
            return cls(__lang__)
    
    @classmethod
    def does_instance_exist(cls, __lang__):
        for instance in cls.__instances__:
            if instance.__lang__ == __lang__:
                return instance
