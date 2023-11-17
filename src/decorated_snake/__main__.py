import sys
from dataclasses import dataclass
from functools import partial
from itertools import count

import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT

from decorated_snake.decorators import apply, call, curry, flip, value

pygame.init()


class Constants:
    def __init__(self, _) -> None:
        pass

    @property
    def WIDTH(self):
        return 500

    @property
    def HEIGHT(self):
        return 500

    @property
    def CELL_SIZE(self):
        return 10


@Constants
def constants():
    pass


@flip
@curry
@value(map)
def fcmap():
    pass


@dataclass
class GameState:
    @value([(20, 20)])
    def snake():
        pass

    @value((constants.CELL_SIZE, 0))
    def snake_dir():
        pass


# Initialize screen
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Snake")


@value(
    {
        K_UP: (0, -constants.CELL_SIZE),
        K_DOWN: (0, constants.CELL_SIZE),
        K_LEFT: (-constants.CELL_SIZE, 0),
        K_RIGHT: (constants.CELL_SIZE, 0),
    }
)
def key_dict():
    pass


def keydown(event, state):
    @partial(state, "snake_dir")
    @value(setattr)
    def set_snake_dir():
        pass

    @apply(set_snake_dir)
    @curry(key_dict.get)
    @value(event.key)
    def dummy():
        pass


def close(*args):
    pygame.quit()
    sys.exit()


@value(
    {
        QUIT: close,
        KEYDOWN: keydown,
    }
)
def event_type_dict():
    pass


def update(state: GameState):
    @list
    @call(lambda e: event_type_dict.get(e.type, lambda *args: None)(e, state))
    @fcmap
    @call()
    @value(pygame.event.get)
    def loop():
        pass

    # Move snake
    new_head = (
        state.snake[0][0] + state.snake_dir[0],
        state.snake[0][1] + state.snake_dir[1],
    )
    state.snake = [new_head] + state.snake[:-1]

    # Draw everything
    screen.fill((0, 0, 0))
    for x, y in state.snake:
        pygame.draw.rect(
            screen, (0, 255, 0), (x, y, constants.CELL_SIZE, constants.CELL_SIZE)
        )

    pygame.display.update()
    pygame.time.delay(150)


def main():
    @list
    @call(update)
    @fcmap
    @call(lambda _: GameState)
    @fcmap
    @count
    @value(0)
    def dummy():
        pass


@apply(lambda x: x.get("__main__", lambda _: None)())
@value({"__main__": main})
def dummy():
    pass
