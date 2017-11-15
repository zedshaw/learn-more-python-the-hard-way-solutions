from calc.run import TOKENS
from calc.scanner import Scanner

code = open("test1.calc").readlines()

def test_Scanner():
    s = Scanner(TOKENS, code)
    s.match('NAME')
    s.match('EQUAL')
    assert s.peek() == 'SPACE'
    s.skip('SPACE')
    s.match('INT')

