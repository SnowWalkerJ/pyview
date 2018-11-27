from ..core import BuiltinWidget


class Card(BuiltinWidget):
    def __init__(self, title, content):
        super(Card, self).__init__()
        self.title = title
        self.content = content

    def tag_(self, attributes):
        return f'<Card title="{self.title}" {attributes}>{self.content}</Card>'
