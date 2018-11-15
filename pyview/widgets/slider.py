import numpy as np
import jinja2
from ..core import Widget


class Slider(Widget):
    def __init__(self, min, max, step=1, value=None, description=None):
        super(Slider, self).__init__()
        self.min = min
        self.max = max
        self.step = step
        self.value = min if value is None else value
        self.options = self.arange(min, max, step)
        self.description = description

    def template(self):
        return jinja2.Template("""
        {% if description %}
        <label for="{{id}}">{{description}}</label>
        {% endif %}
        <Slider id="{{id}}" :min="{{min}}" :max="{{max}}" :step="{{step}}"
            v-on:on-change="this.on_change"
            v-bind:value="this.value"></Slider>
        """).render(description=self.description, id=self.id, min=self.min, max=self.max, step=self.step)

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

    @staticmethod
    def arange(min, max, step):
        result = []
        i = min
        while i <= max:
            result.append(i)
            i += step

        return result
