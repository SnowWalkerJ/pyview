import jinja2
from pyview.core import Document, Widget


class TestWidget(Widget):
    def template(self):
        return "<i-button>a</i-button>"


class TestWidget2(Widget):
    def template(self):
        return "This is raw text"


doc = Document()
doc.add_sheet("Sheet1", TestWidget())
doc.add_sheet("Sheet2", TestWidget2())
with open("samples/simple.html", "w") as f:
    f.write(doc.render())
