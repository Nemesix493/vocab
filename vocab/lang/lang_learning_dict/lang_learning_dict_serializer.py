from ...serializers.base import BaseSerializer
from .lang_learning_dict import LangLearningDict
from ..lang import LangEnum

class LangLearningDictSerializer(BaseSerializer):
    def gen_data(self):
        if self._obj is None:
            raise ValueError('You can\'t load data from None Object')
        self._data = {
            '__lang__': str(self.obj.__lang__.value),
            **self.obj
        }


    def gen_obj(self):
        if self._data is None:
            raise ValueError('You can\'t load object from None Data Object')
        self._obj = self.model_class(
            **{
                **{
                    key: val 
                    for key, val in self.data.items()
                    if key != '__lang__'
                },
            '__lang__': LangEnum._value2member_map_[self.data['__lang__']]
            }
        )
