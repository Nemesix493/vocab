from .base import BaseSerializer


class LangDictSerializer(BaseSerializer):
    @property
    def data(self):
        return self.obj