import jinja2
from pyview.core import Document, Widget
from pyview.widgets.grid import Grid


class Text(Widget):
    def __init__(self, text):
        super(Text, self).__init__()
        self.text = text

    def template(self):
        return self.text


doc = Document()
grid = Grid(2, 2)
grid.add(Text("This is left top"))
grid.add(Text("This is right top"))
grid.add(Text("This is left bottom"))
grid.add(Text("This is right bottom"))
doc.add_sheet("Grid", grid)
with open("examples/grid.html", "w") as f:
    f.write(doc.render())
