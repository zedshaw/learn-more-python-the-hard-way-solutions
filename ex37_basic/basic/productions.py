class Production(object):
    def analyze(self, world):
        """Implement your analyzer here."""

    def interpret(self, world):
        """Implement your interpreter here."""


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

class AssignExpr(Expr):

    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def interpret(self, world):
        world.variables[self.name.name] = self.expr
        return self.expr.interpret(world)

    def __repr__(self):
        return f"{self.name} = {self.expr}"


class IntExpr(Expr):
    def __init__(self, token):
        self.integer = int(token[1])
        self.token = token

    def __repr__(self):
        return f"IntExpr({self.integer})"

    def interpret(self, world):
        return self.integer


class InfixExpr(Expr):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def analyze(self, world):
        self.left.analyze(world)
        self.right.analyze(world)

    def interpret(self, world):
        left_n = self.left.interpret(world) 
        right_n = self.right.interpret(world)
        if self.op == 'PLUS':
            return left_n + right_n
        elif self.op == 'MINUS':
            return left_n + right_n
        elif self.op == 'DIV':
            return left_n / right_n
        elif self.op == 'MULT':
            return left_n * right_n
        else:
            assert False, "Nope."

    def __repr__(self):
        return f"AddExpr({self.left}, {self.right})"

class PrintExpr(Expr):

    def __init__(self, expr):
        self.expr = expr

    def interpret(self, world):
        print(self.expr.interpret(world))

class GotoExpr(Expr):
    def __init__(self, expr):
        self.expr = expr

    def interpret(self, world):
        world.goto(self.expr.interpret(world))

