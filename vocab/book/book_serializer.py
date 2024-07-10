from ..serializers import BaseSerializer

from ..lang.lang import LangEnum

class BookSerializer(BaseSerializer):

    def gen_data(self):
        if self._obj is None:
            raise ValueError('You can\'t load data from None Object')
        keys = ['name', 'title', 'lang', 'proper_nouns', 'occurences']
        self._data = {
            **{
                key: self.obj.__getattribute__(key)
                for key in keys
                if key != 'lang'
            },
            **{
                'lang': self.obj.lang.value
            }
        }


    def gen_obj(self):
        if self._data is None:
            raise ValueError('You can\'t load object from None Data Object')
        
        self._obj = self.model_class(**{
            **{
                key: val
                for key, val in self._data.items()
                if key != 'lang'
            },
            **{
                'lang': LangEnum._value2member_map_.get(self._data['lang'])
            }
        })