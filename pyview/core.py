import uuid
import jinja2
from .tree import DependencyTree


class Widget:
    def __init__(self):
        self.children = []
        self.id = "Widget" + uuid.uuid4().hex
        self.depends_on = []

    def head(self):
        pass

    def data(self):
        return "{}"

    def methods(self):
        return "{}"

    def template(self):
        return ""

    def props(self):
        return "[]"

    def components(self):
        return []

    def script(self):
        template = jinja2.Template("""
        {
            data: function () { return {{data}}; },
            methods: {{methods}},
            props: {{props}},
            template: `<div>{{html}}<div>`,
            components: { {{components}} }
        }""")
        return template.render(
            id=self.id,
            data=self.data(),
            methods=self.methods(),
            props=self.props(),
            components=", ".join((comp.id for comp in self.components() if not isinstance(comp, BuiltinWidget))),
            html=self.template())

    def style(self):
        return ""

    def render(self):
        # heads = self.head()
        # if heads:
        #     self.document.heads.update(set(heads.split("\n")))
        template = """
        <script> var {{id}} = Vue.component('{{id}}', {{script}}); </script>"""
        return jinja2.Template(template).render(id=self.id, script=self.script())

    def tag_(self, attributes):
        return f"<{self.id}{attributes} />"

    def tag(self, **kwargs):
        attributes = []
        for key, value in kwargs.items():
            if key[:2] == 'b_':
                key = ":" + key[2:]
            elif key[:2] == "e_":
                key = "@" + key[2:]
            elif key[:2] == "v_":
                key = key.replace("_", "-")
            attributes.append(f' {key}="{value}"')
        attributes = "".join(attributes)
        return self.tag_(attributes)

    def __repr__(self):
        return self.tag()


class BuiltinWidget(Widget):
    def __init__(self):
        super(BuiltinWidget, self).__init__()

    def render(self):
        return ""


class Document:
    """文档"""
    def __init__(self):
        self.sheets = []
        self.frame = Frame(self.sheets)
        self.dependencies = DependencyTree()

    def add_sheet(self, name: str, sheet: Widget):
        self.sheets.append((name, sheet))
        self.dependencies.add(sheet)

    def render_dependencies(self):
        return "\n\n".join(widget.render() for widget in self.dependencies.resolve_dependencies())

    def render(self):
        return jinja2.Template("""<!DOCTYPE html>
        <html>
        <head>
        <script src="http://vuejs.org/js/vue.min.js"></script>
        <link rel="stylesheet" href="http://unpkg.com/iview/dist/styles/iview.css">
        <script src="http://unpkg.com/iview/dist/iview.min.js"></script>
        <style>
            body {
                padding: 0 5% 0 5%;
                text-align: center;
            }
        </style>
        <head>
        <body>
        {{ dependencies }}
        {{ frame }}
        <div id="backtop"></div>
        <script>
        new Vue({
            el: 'backtop',
            template: '<BackTop></BackTop>'
        })
        </script>
        </body>
        </html>""").render(
            dependencies=self.render_dependencies(),
            frame=self.frame.render())


class Frame(Widget):
    def __init__(self, sheets):
        super(Frame, self).__init__()
        self.sheets = sheets
        self.id = "Frame"

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

    def script(self):
        return jinja2.Template("""
        new Vue({
            el: '#frame',
            components: { {{components}} },
            data: {
                tabname: '{{tabs[0][1].id}}'
            },
            template: `{{template}}`
        });""").render(
            tabs=self.sheets,
            components=",".join(sheet.id for name, sheet in self.sheets if not isinstance(sheet, BuiltinWidget)),
            template=self.template())

    def render(self):
        return jinja2.Template("""
        <div id="frame"></div>
        {% if script %} <script> {{script}} </script> {% endif %}
        """).render(id=self.id, script=self.script())
