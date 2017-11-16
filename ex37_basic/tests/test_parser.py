from basic.run import TOKENS, BasicParser, BasicWorld
from basic.scanner import Scanner
from basic.analyzer import BasicAnalyzer
from tests.test_scanner import code

def test_Parser():
    scanner = Scanner(TOKENS, code)
    parser = BasicParser(scanner)
    return parser.parse()


def test_Analyzer():
    variables = {}
    world = BasicWorld(variables)

    script = test_Parser()
    print(script)
    analyzer = BasicAnalyzer(script, world)
    return analyzer.analyze(), world

def test_Interpreter():
    prods, world = test_Analyzer()
    for line_no, prod in prods:
        prod.interpret(world)

