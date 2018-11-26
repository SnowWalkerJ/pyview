# Pyview

Pyview aims at being a substitute of ipywidgets without the support of Jupyter Notebook.
It relies on VueJS and iView, and helps you generate static reports efficiently.

## Examples

```python
from pyview import Document, Widget
from pyview.widgets import *


doc = Document()

tabs = Tabs()

# It's a single-image page
sheet1 = Img("https://assets-cdn.github.com/images/modules/logos_page/Octocat.png")
tabs.add("Octocat", sheet1)

# Sheet2 is an image controlled by a switch
@controlled_function(
    visible=Switch("Visible")
)
def sheet2(visible):
    if visible:
        return Img("https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png")
    else:
        return Widget()

tabs.add("Github", sheet2)

doc.set_frame(tabs)

print(doc.render())

```