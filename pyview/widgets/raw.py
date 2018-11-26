from ..core import BuiltinWidget


class Raw(BuiltinWidget):
    def __init__(self, content=None):
        super(Tag, self).__init__()
        self.content = content

    def tag_(self, attributes):
        return f"<div {attributes}>{self.content}</div>"
