@(lambda m: m.dataclass)
@__import__
@(lambda f: f.__doc__)
def dataclass(): "dataclasses"

@(lambda m: m.decorators.value)
@__import__
@(lambda f: f.__doc__)
def value(): "decosnake.decorators"


@dataclass
class GameState:
    @value([(20, 20), (21, 20), (22, 20), (23, 20)])
    def snake():
        pass

    @value((1, 0))
    def snake_dir():
        pass

    @value((10, 10))
    def apple_pos(self):
        pass
