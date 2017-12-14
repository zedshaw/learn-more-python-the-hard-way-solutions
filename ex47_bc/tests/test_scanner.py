from calc.run import TOKENS
from calc.scanner import Scanner

code = open("test2.calc").readlines()

def test_Scanner():
    s = Scanner(TOKENS, code)

