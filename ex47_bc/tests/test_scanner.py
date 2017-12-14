from calc.run import TOKENS
from calc.scanner import Scanner

code = open("test1.calc").readlines()

def test_Scanner():
    s = Scanner(TOKENS, code)

