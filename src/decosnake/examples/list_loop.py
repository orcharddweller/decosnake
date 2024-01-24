@(lambda m: m.count)
@__import__
@(lambda f: 'itertools')
def count(): pass

@(lambda m: m.decorators.call)
@__import__
@(lambda f: 'decosnake.decorators')
def call(): pass
@(lambda m: m.decorators.curry)
@__import__
@(lambda f: 'decosnake.decorators')
def curry(): pass
@(lambda m: m.decorators.flip)
@__import__
@(lambda f: 'decosnake.decorators')
def flip(): pass
@(lambda m: m.decorators.value)
@__import__
@(lambda f: 'decosnake.decorators')
def value(): pass


@list
@call(lambda x: print(x) and x)
@flip(curry(map))
@count
@value(0)
def loop():
    pass
