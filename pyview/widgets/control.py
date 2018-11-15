import itertools

import jinja2
import ujson

from ..core import Widget


class Controlled(Widget):
    def __init__(self, function, kwargs):
        super(Controlled, self).__init__()
        self.function = function
        self.params = kwargs
        self.depends_on = list(kwargs.values())
        self.keys = list(kwargs.keys())
        self.contents = []
        options = itertools.product(*(self.params[key].options for key in self.keys))
        for params in options:
            kwargs = dict(zip(self.keys, params))
            content = self.function(**kwargs)
            self.depends_on.append(content)
            self.contents.append((self.resolve_params(kwargs), content))

    def template(self):
        return jinja2.Template("""
        <Row>
        <Col span="6">
        {%- for (name, controller) in controllers -%}
            {{controller.tag(v_model=name)}}
        {%- endfor -%}
        </Col>
        <Col span="18">
        {%- for (condition, content) in contents -%}
        {{content.tag(v_if=condition)}}
        {%- endfor -%}
        </Col>
        </Row>
        """).render(controllers=self.params.items(), contents=self.contents)

    def data(self):
        return jinja2.Template("""{
        {%- for (name, widget) in params -%}
        {{name}}: {{ujson.dumps(widget.options[0])}} {%if not loop.last %},{% endif %}
        {%- endfor -%}
        }""").render(params=self.params.items(), ujson=ujson)

    def components(self):
        return [content[1] for content in self.contents]

    @staticmethod
    def resolve_params(kwargs):
        conditions = []
        for key, value in kwargs.items():
            condition = "(this.{} == {})".format(key, ujson.dumps(value))
            conditions.append(condition)
        return "&&".join(conditions)
