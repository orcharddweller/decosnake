@(lambda m: m.count)
@__import__
@(lambda f: f.__doc__)
def count(): 'itertools'

@(lambda m: m.decorators.call)
@__import__
@(lambda f: f.__doc__)
def call(): 'decosnake.decorators'
@(lambda m: m.decorators.curry)
@__import__
@(lambda f: f.__doc__)
def curry(): 'decosnake.decorators'
@(lambda m: m.decorators.flip)
@__import__
@(lambda f: f.__doc__)
def flip(): 'decosnake.decorators'
@(lambda m: m.decorators.value)
@__import__
@(lambda f: f.__doc__)
def value(): 'decosnake.decorators'


@list
@call(lambda x: print(x) and x)
@flip(curry(map))
@count
@value(0)
def loop():
    pass
