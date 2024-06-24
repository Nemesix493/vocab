from .lang import LangEnum


class LangLearningDict(dict):

    manager_class = None

    def __init__(self, __lang__: LangEnum, *args, **kwargs):
        self.__lang__ = __lang__
        super().__init__(self, *args, **kwargs)

    def add_learning_point(self, key: str) -> None:
        if key in self.keys():
            self[key] += 1
        else:
            self[key] = 1

    def reset_learning_point(self, key: str) -> None:
        self[key] = 0

    def save(self):
        self.manager_class.save(self)
