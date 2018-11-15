from copy import copy, deepcopy


class DependencyTree:
    def __init__(self):
        self.dependencies = {}

    def add(self, widget):
        self.dependencies[widget] = copy(widget.depends_on)
        for widget in widget.depends_on:
            if widget not in self.dependencies:
                self.add(widget)

    def resolve_dependencies(self):
        self.backup_dependencies = deepcopy(self.dependencies)
        while self.dependencies:
            for widget, dependencies in self.dependencies.items():
                if not dependencies:
                    yield widget
                    self.remove_dependency(widget)
                    break
        self.dependencies = self.backup_dependencies
        del self.backup_dependencies

    def remove_dependency(self, widget):
        for dependency in self.dependencies.values():
            if widget in dependency:
                dependency.remove(widget)
        del self.dependencies[widget]
