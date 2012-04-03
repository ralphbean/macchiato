from macchiato import percolate

@percolate(main="foo()")
def foo():
    def bar():
        x = 0
        b = 2
        y = x + b
        return y

    print bar()
    return bar()

print foo
