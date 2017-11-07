class Production(object):
    def analyze(self, world):
        """Implement your analyzer here."""

class FuncCall(Production):

    def __init__(self, token, params):
        self.name = token[1]
        self.params = params
        self.token = token

    def analyze(self, world):
        self.params.analyze(world)

    def __repr__(self):
        return f"FuncCall({self.name}: {self.params})"

class Parameters(Production):

    def __init__(self, expressions):
        self.expressions = expressions

    def analyze(self, world):
        for expr in self.expressions:
            expr.analyze(world)

    def __repr__(self):
        return f"Parameters({self.expressions})"

class Expr(Production): pass

class NameExpr(Expr):
    def __init__(self, token):
        self.name = token[1]
        self.token = token

    def __repr__(self):
        return f"NameExpr({self.name})"

class IntExpr(Expr):
    def __init__(self, token):
        self.integer = token[1]
        self.token = token

    def __repr__(self):
        return f"IntExpr({self.integer})"

class AddExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def analyze(self, world):
        self.left.analyze(world)
        self.right.analyze(world)

    def __repr__(self):
        return f"AddExpr({self.left}, {self.right})"

class FuncDef(Production):

    def __init__(self, token, params, body):
        self.name = token[1]
        self.params = params
        self.body = body
        self.token = token

    def analyze(self, world):
        world.functions[self.name] = self

    def __repr__(self):
        return f"FuncDef({self.name}({self.params}): {self.body}"


