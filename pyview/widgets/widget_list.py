from copy import copy

import jinja2

from ..core import BuiltinWidget


class WidgetList(BuiltinWidget):
    def __init__(self, widgets: list=None):
        super(WidgetList, self).__init__()
        if widgets is None:
            widgets = []
        self.widgets = copy(widgets)
        self.depends_on = copy(widgets)

    def add(self, widget):
        self.widgets.append(widget)
        self.depends_on.append(widget)

    def tag_(self, attributes):
        return jinja2.Template("""
        <div {{attributes}}>
        {%- for widget in widgets -%}
            {{widget}}
        {%- endfor -%}
        </div>
        """).render(widgets=self.widgets, attributes=attributes)
