from .base import BaseSerializer


class LangLearningDictSerializer(BaseSerializer):
    @property
    def data(self):
        return self.obj