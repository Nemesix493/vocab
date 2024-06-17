from .lang import LangEnum


class LangDict(dict):
    def __init__(self, lang: LangEnum, *args, **kwargs):
        self.lang = lang
        super().__init__(self, *args, **kwargs)

    def add_learning_point(self, key: str) -> None:
        if key in self.keys():
            self[key] += 1
        else:
            self[key] = 1

    def reset_learning_point(self, key: str) -> None:
        self[key] = 0
