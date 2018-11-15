
import jinja2

from ..core import Widget


class Switch(Widget):
    def __init__(self, description=None):
        super(Switch, self).__init__()
        self.description = description
        self.options = [True, False]

    def template(self):
        return jinja2.Template("""{% if description %}
        <label for="{{id}}">{{description}}</label>
        {% endif %}
        <i-switch v-on:on-change="this.on_change"
            v-bind:value="this.value" />
        """).render(id=self.id,
                    description=self.description)

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
