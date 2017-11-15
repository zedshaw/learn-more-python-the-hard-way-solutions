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
        """root = *(expression)"""
        return self.expression()

    def expression(self):
        """expression = name / assign / infix / integer"""
        start = self.peek()

        if start == 'NAME':
            name = self.match('NAME')
            nameexpr = prod.NameExpr(name)

            op = self.peek()

            if op in ['PLUS', 'MINUS', 'DIV', 'MULT']:
                return self.infix(nameexpr, op)
            elif op == 'EQUAL':
                return self.assign(nameexpr)
            else:
                return nameexpr
        elif start == 'INTEGER':
            number = self.match('INTEGER')
            numexpr = prod.IntExpr(number)
            op = self.peek()

            if op in ['PLUS', 'MINUS', 'DIV', 'MULT']:
                return self.infix(numexpr, op)
            else:
                return numexpr
        else:
            assert False, "Syntax error %r" % start

    def assign(self, name):
        self.skip('EQUAL')
        right = self.expression()
        return prod.AssignExpr(name, right)

    def infix(self, left, op):
        """plus = expression PLUS expression"""
        self.match(op)
        right = self.expression()
        return prod.InfixExpr(left, op, right)

class CalcWorld(object):

    def __init__(self, variables):
        self.variables = variables
        self.functions = {}

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
        print(prod.interpret(world))

if __name__ == "__main__":
    _, script = sys.argv

    run(open(script).readlines())
