from dataclasses import dataclass
from typing import Any


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
