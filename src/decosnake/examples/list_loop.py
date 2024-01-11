from itertools import count

from decosnake.decorators import call, curry, flip, value


@list
@call(lambda x: print(x) and x)
@flip(curry(map))
@count
@value(0)
def loop():
    pass
