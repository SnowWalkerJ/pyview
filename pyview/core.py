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

    def script(self, is_frame=False):
        template = jinja2.Template("""
        {
            {%- if is_frame -%}el: '#frame',{%- endif -%}
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
            is_frame=is_frame,
            components=", ".join((comp.id for comp in self.components() if not isinstance(comp, BuiltinWidget))),
            html=self.template())

    def style(self):
        return ""

    def render(self, is_frame=False):
        if is_frame:
            return jinja2.Template("""
            <script> new Vue({{script}}); </script>
            """).render(script=self.script(is_frame))
        else:
            return jinja2.Template("""
            <script> var {{id}} = Vue.component('{{id}}', {{script}}); </script>
            """).render(id=self.id, script=self.script(is_frame))

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
        self.frame = None

    def render_dependencies(self):
        dependencies = DependencyTree()
        for widget in self.frame.depends_on:
            dependencies.add(widget)
        return "\n\n".join(widget.render() for widget in dependencies.resolve_dependencies())

    def set_frame(self, widget):
        self.frame = widget

    def render(self):
        if not self.frame:
            raise ValueError("You must set a frame for document")
        return jinja2.Template("""<!DOCTYPE html>
        <html>
        <head>
        <script src="http://vuejs.org/js/vue.min.js"></script>
        <link rel="stylesheet" href="http://unpkg.com/iview/dist/styles/iview.css">
        <script src="http://unpkg.com/iview/dist/iview.min.js"></script>
        <style>
            body {
                padding: 0 8%;
            }
        </style>
        <head>
        <body>
        {{ dependencies }}
        <div id="frame"/>
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
            frame=self.frame.render(True))
