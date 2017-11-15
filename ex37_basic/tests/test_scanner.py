from basic.run import TOKENS
from basic.scanner import Scanner

code = open("test1.bs").readlines()

def test_Scanner():
    s = Scanner(TOKENS, code)

