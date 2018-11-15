import jinja2

from ..core import Widget


class Collapse(Widget):
    def __init__(self):
        super(Collapse, self).__init__()
        self.widgets = []

    def add(self, label, widget):
        self.widgets.append((label, widget))
        self.depends_on.append(widget)

    def template(self):
        return jinja2.Template("""
        <Collapse>
        {%- for (i, (label, widget)) in widgets -%}
            <Panel name="{{i}}">
            {{label}}
            <{{widget.id}} slot="content" />
            </Panel>
        {%- endfor -%}
        </Collapse>
        """).render(widgets=enumerate(self.widgets))