@(lambda m: m.dataclass)
@__import__
@(lambda f: f.__doc__)
def dataclass(): 'dataclasses'

@(lambda m: m.Any)
@__import__
@(lambda f: f.__doc__)
class Any: 'typing'


@dataclass
class writer:
    v: Any
    content: list

    @classmethod
    def unit(cls, v):
        return writer(v=v, content=[])

    @classmethod
    def bind(cls, ma: "writer"):
        def func(f):
            result = f(ma.v)
            return writer(v=result.v, content=ma.content + result.content)

        return func
