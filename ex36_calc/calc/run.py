import re
from calc.scanner import Scanner
from calc.parser import Parser
from calc.analyzer import CalcAnalyzer
from calc import productions as prod
import sys

TOKENS = [
(re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
(re.compile(r"^[0-9]+"),                 "INTEGER"),
(re.compile(r"^\="),                     "EQUAL"),
(re.compile(r"^\+"),                     "PLUS"),
(re.compile(r"^\-"),                     "MINUS"),
(re.compile(r"^\*"),                     "MULT"),
(re.compile(r"^/"),                     "DIV"),
(re.compile(r"^\s+"),                     "SPACE"),
]

class CalcParser(Parser):

    def root(self):
        """root = *(funccal / funcdef)"""
        assert False, "Nope"

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

class CalcWorld(object):

    def __init__(self, variables):
        self.variables = variables
        self.functions = {}
        self.functions['print'] = prod.PrintFuncDef()

    def clone(self):
        """Sort of a lame way to implement scope."""
        temp = CalcWorld(self.variables.copy())
        temp.functions = self.functions
        return temp


def run(script):
    scanner = Scanner(TOKENS, script)
    parser = CalcParser(scanner)
    parse_tree = parser.parse()
    world = CalcWorld({})
    analyzer = CalcAnalyzer(parse_tree, world)
    prods = analyzer.analyze()
    for prod in prods:
        prod.interpret(world)

if __name__ == "__main__":
    _, script = sys.argv

    run(open(script).readlines())
