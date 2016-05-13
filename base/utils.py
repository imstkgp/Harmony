from model_utils import Choices
from haystack.utils import Highlighter

class NiceChoices(Choices):
    def __init__(self, *args, **kwargs):
        super(NiceChoices,self).__init__(*args,**kwargs)
        self._reverse_display_map = dict([(str(i[1]).lower().replace(" ","_"),i[0]) for i in self._display_map.items()])

    def find(self,i):
        return self._reverse_display_map.get(str(i).lower().replace(" ","_"),0)


def execute_highlighter(query, text_key, results):
    highlight = Highlighter(query)
    for result in results:
        highlight.text_block = result.get_additional_fields().get(text_key, "")
        highlight_locations = highlight.find_highlightable_words()
        result.highlight_locations = []
        for q, locations in highlight_locations.iteritems():
            result.highlight_locations.extend([[location, location + len(q)] for location in locations])