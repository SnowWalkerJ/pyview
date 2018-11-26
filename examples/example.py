from pyview import Document
from pyview.widgets import Tabs
from tags import sheet as sheet1
from controls import sheet as sheet2


doc = Document()


tabs = Tabs()

tabs.add("tags", sheet1)
tabs.add("controls", sheet2)

doc.set_frame(tabs)

with open("examples/example.html", "w") as f:
    f.write(doc.render())
