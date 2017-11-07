class Production(object):
    def analyze(self, world):
        """Implement your analyzer here."""

    def interpret(self, world):
        """Implement your interpreter here."""

class FuncCall(Production):

    def __init__(self, token, params):
        self.name = token[1]
        self.params = params
        self.token = token

    def analyze(self, world):
        self.params.analyze(world)

    def interpret(self, world):
        funcdef = world.functions[self.name]
        funcdef.call(world, self.params)

    def __repr__(self):
        return f"FuncCall({self.name}: {self.params})"

class Parameters(Production):

    def __init__(self, expressions):
        self.expressions = expressions

    def analyze(self, world):
        for expr in self.expressions:
            expr.analyze(world)

    def interpret(self, world):
        return [x.interpret(world) for x in self.expressions]

    def __repr__(self):
        return f"Parameters({self.expressions})"

class Expr(Production): pass

class NameExpr(Expr):
    def __init__(self, token):
        self.name = token[1]
        self.token = token

    def interpret(self, world):
        # This should point at an IntExpr for now
        ref = world.variables.get(self.name)
        return ref.interpret(world)

    def __repr__(self):
        return f"NameExpr({self.name})"

class IntExpr(Expr):
    def __init__(self, token):
        self.integer = int(token[1])
        self.token = token

    def __repr__(self):
        return f"IntExpr({self.integer})"

    def interpret(self, world):
        return self.integer


class AddExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def analyze(self, world):
        self.left.analyze(world)
        self.right.analyze(world)

    def interpret(self, world):
        return self.left.interpret(world) + self.right.interpret(world)


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

    def call(self, world, params):
        params = params or Parameters()

        scope = world.clone()
        for i, p in enumerate(self.params.expressions):
            scope.variables[p.name] = params.expressions[i]

        for line in self.body:
            line.interpret(scope)

class PrintFuncDef(Production):

    def call(self, world, params):
        print(*params.interpret(world))


