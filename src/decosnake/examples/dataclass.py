from dataclasses import dataclass

from decosnake.decorators import value


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
