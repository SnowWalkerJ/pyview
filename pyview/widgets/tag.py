from ..core import BuiltinWidget


class Tag(BuiltinWidget):
    def __init__(self, name):
        super(Tag, self).__init__()
        self.name = name

    def tag_(self, attributes):
        return f"<{self.name}{attributes} />"
