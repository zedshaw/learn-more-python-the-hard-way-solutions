class Production(object):
    def analyze(self, world):
        """Implement your analyzer here."""

class FuncCall(Production):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def analyze(self, world):
        self.params.analyze(world)

class Parameters(Production):

    def __init__(self, expressions):
        self.expressions = expressions

    def analyze(self, world):
        for expr in self.expressions:
            expr.analyze(world)

class Expr(Production): pass

class NameExpr(Expr):
    def __init__(self, name):
        self.name = name

class IntExpr(Expr):
    def __init__(self, integer):
        self.integer = integer

class AddExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def analyze(self, world):
        self.left.analyze(world)
        self.right.analyze(world)

class FuncDef(Production):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def analyze(self, world):
        world.functions[self.name] = self

