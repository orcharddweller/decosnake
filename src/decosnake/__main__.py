import random
import sys
from dataclasses import dataclass
from functools import partial, reduce
from itertools import count, product

import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT

from decosnake.decorators import call, curry, delay, flip, unpack, value
from decosnake.writer import writer

pygame.init()


class Constants:
    def __init__(self, _) -> None:
        pass

    @property
    def WIDTH(self):
        return 32

    @property
    def HEIGHT(self):
        return 32

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
    @value([(20, 20), (21, 20), (22, 20), (23, 20)])
    def snake():
        pass

    @value((1, 0))
    def snake_dir():
        pass

    @value((10, 10))
    def apple_pos(self):
        pass


@pygame.display.set_mode
@value((constants.WIDTH * constants.CELL_SIZE, constants.HEIGHT * constants.CELL_SIZE))
@pygame.display.set_caption
@value("Snake")
def screen():
    pass


@value(
    {
        K_UP: (0, -1),
        K_DOWN: (0, 1),
        K_LEFT: (-1, 0),
        K_RIGHT: (1, 0),
    }
)
def key_dict():
    pass


def keydown(event, state: GameState):
    @call(state, "snake_dir")
    @curry(partial)
    @value(setattr)
    def set_snake_dir():
        pass

    set_snake_dir(key_dict[event.key])

    @set_snake_dir
    @key_dict.get
    @value(event.key)
    def dummy():
        pass


def close(*_):
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


@count
@value(0)
def count_gen():
    pass


def reset_apple(state: GameState):
    @call("apple_pos")
    @curry
    @curry(setattr)
    @value(state)
    def set_apple_pos():
        pass

    @set_apple_pos
    @random.choice
    @list
    @call(lambda x: x not in state.snake)
    @flip(curry(filter))
    @unpack(product)
    @call(range)
    @fcmap
    @value((constants.WIDTH, constants.HEIGHT))
    def dummy():
        pass


def draw(state: GameState):
    @call()
    @value(pygame.display.update)
    @(lambda x: pygame.draw.rect(screen, (255, 0, 0), x))
    @(lambda x: tuple(map(lambda y: y * constants.CELL_SIZE, x)))
    @value((*state.apple_pos, 1, 1))
    @list
    @call(lambda x: pygame.draw.rect(screen, (0, 255, 0), x))
    @fcmap
    @call(lambda x: tuple(map(lambda y: y * constants.CELL_SIZE, x)))
    @fcmap
    @call(lambda x: (*x, 1, 1))
    @fcmap
    @value(state.snake)
    @screen.fill
    @value((0, 0, 0))
    def dummy():
        pass

    return state


@delay(1000)
def game_over():
    @call()
    @value(GameState)
    def state():
        pass

    return state


@call(count_gen, GameState())
@curry(reduce)
@delay(150)
def update(state: GameState, _step: int):
    @list
    @call(lambda e: event_type_dict.get(e.type, lambda *args: None)(e, state))
    @fcmap
    @call()
    @value(pygame.event.get)
    def loop():
        pass

    @tuple
    @call(sum)
    @fcmap
    @call(state.snake_dir)
    @curry(zip)
    @state.snake.__getitem__
    @value(-1)
    def new_head():
        pass

    @new_head.__eq__
    @value(state.apple_pos)
    def apple_eaten():
        pass

    @call(state)
    @{True: reset_apple, False: lambda _: None}.get
    @value(apple_eaten)
    def dummy():
        pass

    @value(lambda x: [x])
    def list_wrap():
        pass

    @call(state, "snake")
    @curry(partial)
    @value(setattr)
    def set_snake():
        pass

    @set_snake
    @{True: state.snake, False: state.snake[1:]}.get
    @value(apple_eaten)
    def dummy2():
        pass

    @draw
    @call()
    @{True: game_over, False: lambda: state.snake.append(new_head) or state}.get
    @any
    @call("content")
    @curry(getattr)
    @call(lambda x: writer(x, [state.snake.__contains__(x)]))
    @writer.bind
    @call(lambda x: writer(x, [x[0].__ge__(constants.WIDTH)]))
    @writer.bind
    @call(lambda x: writer(x, [x[1].__ge__(constants.HEIGHT)]))
    @writer.bind
    @call(lambda x: writer(x, [x[1].__lt__(0)]))
    @writer.bind
    @call(lambda x: writer(x, [x[0].__lt__(0)]))
    @writer.bind
    @writer.unit
    @value(new_head)
    def state():
        pass

    return state
