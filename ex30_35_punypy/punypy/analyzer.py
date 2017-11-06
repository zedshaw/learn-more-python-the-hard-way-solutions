
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
