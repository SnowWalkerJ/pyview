import numpy as np
import jinja2
from ..core import BuiltinWidget


class Slider(BuiltinWidget):
    def __init__(self, min, max, step=1, value=None, description=None):
        super(Slider, self).__init__()
        self.min = min
        self.max = max
        self.step = step
        self.value = min if value is None else value
        self.options = self.arange(min, max, step)
        self.description = description

    def tag_(self, attributes):
        return jinja2.Template("""
        <Slider id="{{id}}" :min="{{min}}" :max="{{max}}" :step="{{step}}"
            {{attributes}}></Slider>
        """).render(description=self.description, id=self.id, 
                    min=self.min, max=self.max, step=self.step,
                    attributes=attributes)

    @staticmethod
    def arange(min, max, step):
        result = []
        i = min
        while i <= max:
            result.append(i)
            i += step

        return result
