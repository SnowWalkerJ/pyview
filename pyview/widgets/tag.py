from ..core import BuiltinWidget


class Tag(BuiltinWidget):
    def __init__(self, name, content=None):
        super(Tag, self).__init__()
        self.name = name
        self.content = content

    def tag_(self, attributes):
        if self.content is not None:
            return f"<{self.name}{attributes}>{self.content}</{self.name}>"
        else:
            return f"<{self.name}{attributes} />"
