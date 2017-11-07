from punypy_scanner import Scanner
import re

code = [
"def hello(x, y):",
"    print(x + y)",
"hello(10, 20)",
]

TOKENS = [
(re.compile(r"^def"),                    "DEF"),
(re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
(re.compile(r"^[0-9]+"),                 "INTEGER"),
(re.compile(r"^\("),                     "LPAREN"),
(re.compile(r"^\)"),                     "RPAREN"),
(re.compile(r"^\+"),                     "PLUS"),
(re.compile(r"^:"),                      "COLON"),
(re.compile(r"^,"),                      "COMMA"),
(re.compile(r"^\s+"),                    "INDENT"),
]


def test_Scanner():
    s = Scanner(TOKENS, code)
    assert s.tokens[0][0] == 'DEF'
    assert s.tokens[1][0] == 'INDENT'
    assert s.tokens[2][0] == 'NAME'
    assert s.tokens[2][1] == 'hello'

