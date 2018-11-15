import ujson
import jinja2

from ..core import BuiltinWidget


class Radio(BuiltinWidget):
    def __init__(self, options=[], description=None):
        super(Radio, self).__init__()
        self.description = description
        if isinstance(options, list):
            options = dict(zip(options, options))
        self.options = options

    def tag_(self, attributes):
        return jinja2.Template("""{% if description -%}
        <label for="{{id}}">{{description}}</label>
        {%- endif %}
        <RadioGroup{{attributes}}>
        {% for (key, label) in options -%}
        <Radio :label="{{ujson.dumps(key)}}">{{ label }}</Radio>
        {%- endfor %}
        </RadioGroup>
        """).render(id=self.id,
                    description=self.description,
                    ujson=ujson,
                    attributes=attributes,
                    options=self.options.items())
