import re
from punypy.scanner import Scanner
from punypy.parser import Parser
from punypy.analyzer import PunyPyAnalyzer
from punypy import productions as prod
import sys

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


class PunyPyParser(Parser):

    def root(self):
        """root = *(funccal / funcdef)"""
        first = self.peek()

        if first == 'DEF':
            return self.function_definition()
        elif first == 'NAME':
            name = self.match('NAME')
            second = self.peek()

            if second == 'LPAREN':
                return self.function_call(name)
            else:
                assert False, f"{second} is Not a FUNCDEF or FUNCCALL"

    def function_definition(self):
        """
        funcdef = DEF name LPAREN params RPAREN COLON body
        I ignore body for this example 'cause that's hard.
        I mean, so you can learn how to do it.
        """
        self.skip('DEF')
        name = self.match('NAME')
        self.match('LPAREN')
        params = self.parameters()
        self.skip('RPAREN', 'COLON')
        body = self.function_body()
        return prod.FuncDef(name, params, body)

    def function_body(self):
        body = []
        while self.skip("INDENT"):
            body.append(self.expression())
        return body

    def parameters(self):
        """params = expression *(COMMA expression)"""
        params = []
        start = self.peek()
        while start != 'RPAREN':
            params.append(self.expression())
            start = self.peek()
            if start != 'RPAREN':
                assert self.skip('COMMA')
        return prod.Parameters(params)

    def function_call(self, name):
        """funccall = name LPAREN params RPAREN"""
        self.match('LPAREN')
        params = self.parameters()
        self.match('RPAREN')
        return prod.FuncCall(name, params)

    def expression(self):
        """expression = name / funccall / plus / integer"""
        start = self.peek()

        if start == 'NAME':
            name = self.match('NAME')
            nameexpr = prod.NameExpr(name)

            expr = self.peek()

            if expr == 'PLUS':
                return self.plus(nameexpr)
            elif expr == 'LPAREN':
                return self.function_call(name)
            else:
                return nameexpr
        elif start == 'INTEGER':
            number = self.match('INTEGER')
            numexpr = prod.IntExpr(number)
            if self.peek() == 'PLUS':
                return self.plus(numexpr)
            else:
                return numexpr
        else:
            assert False, "Syntax error %r" % start

    def plus(self, left):
        """plus = expression PLUS expression"""
        self.match('PLUS')
        right = self.expression()
        return prod.AddExpr(left, right)

class PunyPyWorld(object):

    def __init__(self, variables):
        self.variables = variables
        self.functions = {}
        self.functions['print'] = prod.PrintFuncDef()

    def clone(self):
        """Sort of a lame way to implement scope."""
        temp = PunyPyWorld(self.variables.copy())
        temp.functions = self.functions
        return temp


def run(script):
    scanner = Scanner(TOKENS, script)
    parser = PunyPyParser(scanner)
    parse_tree = parser.parse()
    world = PunyPyWorld({})
    analyzer = PunyPyAnalyzer(parse_tree, world)
    prods = analyzer.analyze()
    for prod in prods:
        prod.interpret(world)

if __name__ == "__main__":
    _, script = sys.argv

    run(open(script).readlines())
