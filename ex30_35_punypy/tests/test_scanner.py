from punypy.run import TOKENS
from punypy.scanner import Scanner

code = [
"def hello(x, y):",
"    print(x + y)",
"hello(10, 20)",
]


def test_Scanner():
    s = Scanner(TOKENS, code)
    assert s.skip("DEF")
    assert s.match("NAME")[1] == "hello"
    assert s.skip("LPAREN")
    assert s.peek() == "NAME"
    assert s.match("NAME")[1] == "x"
    assert s.skip("COMMA")
    assert s.match("NAME")[1] == "y"
    assert s.skip("RPAREN", "COLON")
    assert s.match("INDENT")[1] == "    "
    assert s.match("NAME")[1] == "print"
    assert s.skip("LPAREN")
    assert s.match("NAME")[1] == "x"
    assert s.match("PLUS")[0] == "PLUS"
    assert s.match("NAME")[1] == "y"
    assert s.skip("RPAREN")
    assert s.peek() != "INDENT"
    assert s.match("NAME")[1] == "hello"
    assert s.skip("LPAREN")
    assert s.match("INTEGER")[1] == "10"
    assert s.skip("COMMA")
    assert s.match("INTEGER")[1] == "20"
    assert s.skip("RPAREN")


