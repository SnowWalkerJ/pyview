import random

import jinja2
import matplotlib.pyplot as plt

from pyview.core import Document, Widget
from pyview.widgets.slider import Slider
from pyview.widgets.radio import Radio
from pyview.widgets.img import Img
from pyview.widgets.functions import controlled_function


class TestWidget(Widget):
    def template(self):
        return "<i-button>a</i-button>"


class TestWidget2(Widget):
    def template(self):
        return "This is raw text"


@controlled_function(
    yes=Radio([True, False], "yes"),
    val=Slider(1, 3, 1, 1, description="点的数量")
)
def tests(yes, val=10):
    Y = [random.random() for _ in range(val)]
    X = [random.random() for _ in range(val)]
    fig = plt.figure()
    if yes:
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(X, Y)
    return Img(fig)


doc = Document()
doc.add_sheet("Sheet1", tests)
doc.add_sheet("Sheet2", TestWidget())
doc.add_sheet("Sheet3", TestWidget2())
with open("examples/controlled.html", "w") as f:
    f.write(doc.render())
