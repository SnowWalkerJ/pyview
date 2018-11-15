import jinja2
from pyview.core import Document, Widget
from pyview.widgets.collapse import Collapse


class Text(Widget):
    def __init__(self, text):
        super(Text, self).__init__()
        self.text = text

    def template(self):
        return self.text


doc = Document()
collapse = Collapse()
collapse.add("left top", Text("This is left top"))
collapse.add("right top", Text("This is right top"))

doc.add_sheet("Collapse", collapse)
with open("examples/collapse.html", "w") as f:
    f.write(doc.render())
