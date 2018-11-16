from copy import copy

import jinja2

from ..core import Widget, BuiltinWidget


class Tabs(Widget):
    def __init__(self, sheets=None):
        super(Tabs, self).__init__()
        self.sheets = copy(sheets) if sheets else []

    def add(self, name, widget):
        self.sheets.append((name, widget))
        self.depends_on.append(widget)

    def template(self):
        return jinja2.Template("""
        <Tabs :value="tabname">
            {% for name, sheet in tabs %}
            <TabPane label="{{name}}" name="{{sheet.id}}">
                {{sheet}}
            </TabPane>
            {% endfor %}
        </Tabs>
        """).render(tabs=self.sheets)

    def data(self):
        return jinja2.Template("""{
            tabname: '{{tab1}}'
        }""").render(tab1=self.sheets[0][1].id)
