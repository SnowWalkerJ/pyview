
import jinja2

from ..core import BuiltinWidget


class Switch(BuiltinWidget):
    def __init__(self, description=None):
        super(Switch, self).__init__()
        self.description = description
        self.options = [True, False]

    def tag_(self, attributes):
        return jinja2.Template("""{% if description %}
        <label for="{{id}}">{{description}}</label>
        {% endif %}
        <i-switch id="{{id}}"{{attributes}} />
        """).render(id=self.id,
                    attributes=attributes,
                    description=self.description)
