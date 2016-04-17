from model_utils import Choices

class NiceChoices(Choices):
    def __init__(self, *args, **kwargs):
        super(NiceChoices,self).__init__(*args,**kwargs)
        self._reverse_display_map = dict([(str(i[1]).lower().replace(" ","_"),i[0]) for i in self._display_map.items()])

    def find(self,i):
        return self._reverse_display_map.get(str(i).lower().replace(" ","_"),0)

