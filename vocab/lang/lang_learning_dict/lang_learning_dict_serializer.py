from ...serializers.base import BaseSerializer
from .lang_learning_dict import LangLearningDict

class LangLearningDictSerializer(BaseSerializer):
    def gen_data(self):
        if self._obj is None:
            raise ValueError('You can\'t load data from None Object')
        self._data = {
            '__lang__': self.obj.__lang__,
            **self.obj
        }


    def gen_obj(self):
        if self._data is None:
            raise ValueError('You can\'t load object from None Data Object')
        self._obj = self.model_class(**self.data)