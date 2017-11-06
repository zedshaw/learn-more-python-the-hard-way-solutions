from punypy.run import TOKENS, PunyPyParser, PunyPyWorld
from punypy.scanner import Scanner
from punypy.analyzer import PunyPyAnalyzer
from test_scanner import code

def test_Parser():
    scanner = Scanner(TOKENS, code)
    parser = PunyPyParser(scanner)
    return parser.parse()


def test_Analyzer():
    variables = {}
    world = PunyPyWorld(variables)
    # simulate hello(10 + 20)
    script = test_Parser()
    analyzer = PunyPyAnalyzer(script, world)
    analyzer.analyze()
