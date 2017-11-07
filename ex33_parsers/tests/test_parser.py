from punypy.run import TOKENS, PunyPyParser, PunyPyWorld
from punypy.scanner import Scanner
from tests.test_scanner import code

def test_Parser():
    scanner = Scanner(TOKENS, code)
    parser = PunyPyParser(scanner)
    return parser.parse()

