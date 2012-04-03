macchiato - easy python to javascript compilation
=================================================

I have no idea if this is going to work.

>>> from macchiato import percolate
>>> @percolate()
... def foo():
...     def bar():
...         x = 0
...         b = 2
...         y = x + b
...         return y
...
...     print bar()
...     return bar()
>>> print foo
... function foo() {
...
...   function bar() {
...     x = 0;
...     b = 2;
...     y = (x + b);
...     return y
...   }
...   console.log(bar());
...   return bar()
... }
