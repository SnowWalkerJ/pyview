import ujson
import jinja2

from ..core import BuiltinWidget


class Select(BuiltinWidget):
    def __init__(self, options=[], description=None):
        super(Select, self).__init__()
        self.description = description
        if isinstance(options, list):
            options = dict(zip(options, options))
        self.options = options

    def tag_(self, attributes):
        return jinja2.Template("""
        <Select{{attributes}}>
        {% for (key, label) in options %}
        <Option :value="{{ujson.dumps(key)}}">{{ label }}</Option>
        {% endfor %}
        </Select>
        """).render(id=self.id,
                    description=self.description,
                    ujson=ujson,
                    attributes=attributes,
                    options=self.options.items())
