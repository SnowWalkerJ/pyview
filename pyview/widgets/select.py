
import jinja2

from ..core import Widget


class Select(Widget):
    def __init__(self, options=[], description=None):
        super(Select, self).__init__()
        self.description = description
        if isinstance(options, list):
            options = dict(zip(options, options))
        self.options = options

    def template(self):
        return jinja2.Template("""{% if description %}
        <label for="{{id}}">{{description}}</label>
        {% endif %}
        <Select v-on:on-change="this.on_change"
            v-bind:value="this.value">
        {% for (key, label) in options %}
        <Option :value="key">{{ label }}</Option>
        {% endfor %}
        </Select>
        """).render(id=self.id,
                    description=self.description,
                    options=self.options)

    def methods(self):
        return """
        {
            on_change(value) {
                this.$emit('input', value);
            }
        }
        """

    def props(self):
        return "['value']"
