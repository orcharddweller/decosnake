@(lambda m: m.wraps)
@__import__
@(lambda f: f.__doc__)
def wraps(): "functools"

@(lambda m: m.Any)
@__import__
@(lambda f: f.__doc__)
class Any: "typing"

@__import__
@(lambda f: f.__name__)
def pygame(): pass


class delay:
    def __init__(self, milliseconds: int):
        self.milliseconds = milliseconds

    def __call__(self, f) -> Any:
        @wraps(f)
        def wrapper(*args, **kwargs):
            pygame.time.delay(self.milliseconds)
            return f(*args, **kwargs)

        return wrapper


class value:
    """Decorator that replaces the assignment operator.

    Example:
    @value(10)
    def apple_pos():
        pass
    """

    def __init__(self, value: Any):
        @(lambda x: setattr(self, "value", x))
        @(lambda x: value)
        def dummy():
            pass

    def __call__(self, _):
        return self.value


class call:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        return func(*self.args, **self.kwargs)


def curry(f):
    return lambda x: lambda *args: f(x, *args)


def flip(f):
    return lambda x: lambda y: f(y)(x)


def unpack(f):
    return lambda x: f(*x)
