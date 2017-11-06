class Production(object):
    def analyze(self, world):
        """Implement your analyzer here."""


class FuncCall(Production):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def analyze(self, world):
        print("> FuncCall: ", self.name)
        self.params.analyze(world)

class Parameters(Production):

    def __init__(self, expressions):
        self.expressions = expressions

    def analyze(self, world):
        print(">> Parameters: ")
        for expr in self.expressions:
            expr.analyze(world)

class Expr(Production): pass

class IntExpr(Expr):
    def __init__(self, integer):
        self.integer = integer

    def analyze(self, world):
        print(">>>> IntExpr: ", self.integer)

class AddExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def analyze(self, world):
        print(">>> AddExpr: ")
        self.left.analyze(world)
        self.right.analyze(world)

class PunyPyWorld(object):

    def __init__(self, variables):
        self.variables = variables
        self.functions = {}

class PunyPyAnalyzer(object):
    def __init__(self, parse_tree, world):
        self.parse_tree = parse_tree
        self.world = world

    def analyze(self):
        for node in self.parse_tree:
            node.analyze(self.world)

variables = {}
world = PunyPyWorld(variables)
# simulate hello(10 + 20)
script = [FuncCall("hello",
            Parameters(
                [AddExpr(IntExpr(10), IntExpr(20))])
            )]
analyzer = PunyPyAnalyzer(script, world)
analyzer.analyze()
