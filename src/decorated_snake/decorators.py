from typing import Any


class value:
    """Decorator that replaces the assignment operator."""

    def __init__(self, value: Any):
        self.value = value

    def __call__(self, _):
        return self.value


class call:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        return func(*self.args, **self.kwargs)


class apply:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def curry(f):
    return lambda x: lambda y: f(x, y)


def flip(f):
    return lambda x: lambda y: f(y)(x)
