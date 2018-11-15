from pyview import Document, Widget
from pyview.widgets import *


doc = Document()

# It's a single-image page
sheet1 = Img("https://assets-cdn.github.com/images/modules/logos_page/Octocat.png")
doc.add_sheet("Octocat", sheet1)

# Sheet2 is an image controlled by a switch
@controlled_function(
    visible=Switch("Visible")
)
def sheet2(visible):
    if visible:
        return Img("https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png")
    else:
        return Widget()

doc.add_sheet("Github", sheet2)

with open("examples/example.html", "w") as f:
    f.write(doc.render())
