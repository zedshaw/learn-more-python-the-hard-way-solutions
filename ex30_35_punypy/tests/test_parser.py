from punypy.run import TOKENS, PunyPyParser
from punypy.scanner import Scanner
from test_scanner import code

def test_Parser():
    scanner = Scanner(TOKENS, code)
    parser = PunyPyParser(scanner)
    results = parser.parse()

    assert results[0]['type'] == 'FUNCDEF'

