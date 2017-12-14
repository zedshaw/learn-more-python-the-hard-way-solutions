
class CalcAnalyzer(object):
    def __init__(self, parse_tree, world):
        self.parse_tree = parse_tree
        self.world = world

    def analyze(self):
        for node in self.parse_tree:
            node.analyze(self.world)

        return self.parse_tree
