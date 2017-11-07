from punypy.run import TOKENS, PunyPyParser, PunyPyWorld
from punypy.scanner import Scanner
from punypy.analyzer import PunyPyAnalyzer
from tests.test_scanner import code

def test_Parser():
    scanner = Scanner(TOKENS, code)
    parser = PunyPyParser(scanner)
    return parser.parse()


def test_Analyzer():
    variables = {}
    world = PunyPyWorld(variables)

    script = test_Parser()
    print(script)
    analyzer = PunyPyAnalyzer(script, world)
    return analyzer.analyze(), world

def test_Interpreter():
    prods, world = test_Analyzer()
    for prod in prods:
        prod.interpret(world)

