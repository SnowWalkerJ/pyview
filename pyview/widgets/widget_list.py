from copy import copy

import jinja2

from ..core import BuiltinWidget


class WidgetList(BuiltinWidget):
    def __init__(self, widgets: list):
        super(WidgetList, self).__init__()
        self.widgets = copy(widgets)
        self.depends_on = copy(widgets)

    def add(self, widget):
        self.widgets.append(widget)
        self.depends_on.append(widget)

    def tag_(self, attributes):
        return jinja2.Template("""
        {%- for widget in widgets -%}
            {{widget}}
        {%- endfor -%}
        """).render(widgets=self.widgets)