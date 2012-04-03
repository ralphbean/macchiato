import ast
import inspect
import StringIO

from macchiato.compiler import Compiler

class percolate(object):
    """ Transmogrifies python functions into javascript """

    def __init__(self, main=None, closure=True):
        self.main = main
        self.closure = closure


    def __call__(self, func):

        # Build our return buffer
        buf = StringIO.StringIO()

        # Get the source from the inspect module
        source = inspect.getsource(func)

        # Strip off the decorator
        # TODO -- there's probably a better AST way to strip the decorator
        source = '\n'.join(source.split('\n')[1:])

        tree = compile(source, '', 'exec', ast.PyCF_ONLY_AST)
        Compiler(tree, buf)
        result = buf.getvalue()

        # Post processing
        if self.main:
            result += '\n' + self.main
            if result[-1] != ';':
                result += ';'

        if self.closure:
            result = "(%s)();" % result

        return result
