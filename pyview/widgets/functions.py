from ..core import Widget
from .control import Controlled


def controlled_function(**params):
    def decorator(func):
        return Controlled(func, params)
    return decorator
