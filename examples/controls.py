import numpy as np
import matplotlib.pyplot as plt

from pyview.core import Widget
from pyview.widgets import *
from pyview.widgets.functions import controlled_function


sheet = WidgetList([
    Tag("h1", "Controlled Function"),
    Tag("p", "This page shows how the keyword parameters are"
             " controlled by Widgets like Switch and Slider"),
    Tag("Divider"),
])


@controlled_function(
    visible=Switch("Visible"),
    npoints=Slider(20, 40, 5, description="Number of points to show")
)
def scatter_plot(visible, npoints):
    if visible:
        data = np.random.randn(npoints, 2)
        x, y = data[:, 0], data[:, 1]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(x, y)
        ax.set_title(f"Scatter plot with {npoints} points")
        return Img(fig)
    else:
        return Widget()

sheet.add(scatter_plot)
