from calc.run import TOKENS, CalcParser, CalcWorld
from calc.scanner import Scanner
from calc.analyzer import CalcAnalyzer
from tests.test_scanner import code

def test_Parser():
    scanner = Scanner(TOKENS, code)
    parser = CalcParser(scanner)
    return parser.parse()


def test_Analyzer():
    variables = {}
    world = CalcWorld(variables)

    script = test_Parser()
    print(script)
    analyzer = CalcAnalyzer(script, world)
    return analyzer.analyze(), world

def test_Interpreter():
    prods, world = test_Analyzer()
    for prod in prods:
        prod.interpret(world)

