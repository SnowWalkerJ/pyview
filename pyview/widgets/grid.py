import jinja2

from ..core import Widget


class Grid(Widget):
    def __init__(self, nrows, ncols, widths=None):
        super(Grid, self).__init__()
        self.nrows = nrows
        self.ncols = ncols
        self.max_size = nrows * ncols
        self.widgets = []
        self.depends_on = []
        MAX_SPAN = 24
        if widths is None:
            self.widths = [MAX_SPAN // ncols] * ncols
        elif len(widths) == ncols - 1 and sum(widths) < MAX_SPAN:
            widths.append(MAX_SPAN - sum(widths))
            self.widths = widths
        elif len(widths) == ncols:
            self.widths = widths

    def add(self, widget: Widget):
        if len(self.widgets) >= self.max_size:
            raise ValueError("Excess max size")
        self.widgets.append(widget)
        self.depends_on.append(widget)

    def components(self):
        return self.depends_on

    def template(self):
        return jinja2.Template("""
        {%- for (i, widget) in widgets -%}
            {%- if i % ncols == 0 -%}
                <Row>
            {%- endif -%}
            <Col span="{{spans[i % ncols]}}">
                {{widget}}
            </Col>
            {%- if i % ncols == ncols-1 -%}
                </Row>
            {%- endif -%}
        {%- endfor -%}
        """).render(widgets=enumerate(self.widgets), spans=self.widths, ncols=self.ncols)
