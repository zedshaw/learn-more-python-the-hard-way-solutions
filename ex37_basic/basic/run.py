import re
from basic.scanner import Scanner
from basic.parser import Parser
from basic.analyzer import BasicAnalyzer
from basic import productions as prod
import sys

TOKENS = [
<<<<<<< HEAD
(re.compile(r"^LET"),    "LET"),
(re.compile(r"^PRINT"),  "PRINT"),
(re.compile(r"^[A-Z_][A-Z0-9_]*"), "NAME"),
(re.compile(r"^[0-9]+"), "INTEGER"),
(re.compile(r"^\="),     "EQUAL"),
(re.compile(r"^\+"),     "PLUS"),
(re.compile(r"^\-"),     "MINUS"),
(re.compile(r"^\*"),     "MULT"),
(re.compile(r"^/"),      "DIV"),
(re.compile(r"^\s+"),    "SPACE"),
=======
(re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
(re.compile(r"^[0-9]+"),                 "INTEGER"),
(re.compile(r"^\="),                     "EQUAL"),
(re.compile(r"^\+"),                     "PLUS"),
(re.compile(r"^\-"),                     "MINUS"),
(re.compile(r"^\*"),                     "MULT"),
(re.compile(r"^/"),                     "DIV"),
(re.compile(r"^\s+"),                     "SPACE"),
>>>>>>> 83a111722c2bfa0a77c1687112f108e7cb6e50b6
]

class BasicParser(Parser):

    def root(self):
        """root = *(expression)"""
        return self.expression()

    def expression(self):
<<<<<<< HEAD
        """expression = name / assign / infix / integer / print"""
        start = self.peek()

        if start == 'NAME':
            nameexpr = self.name()
=======
        """expression = name / assign / infix / integer"""
        start = self.peek()

        if start == 'NAME':
            name = self.match('NAME')
            nameexpr = prod.NameExpr(name)

>>>>>>> 83a111722c2bfa0a77c1687112f108e7cb6e50b6
            op = self.peek()

            if op in ['PLUS', 'MINUS', 'DIV', 'MULT']:
                return self.infix(nameexpr, op)
<<<<<<< HEAD
            else:
                return nameexpr
        elif start == 'LET':
            return self.assign()
        elif start == 'PRINT':
            return self.print()
        elif start == 'INTEGER':
            numexpr = self.integer()
=======
            elif op == 'EQUAL':
                return self.assign(nameexpr)
            else:
                return nameexpr
        elif start == 'INTEGER':
            number = self.match('INTEGER')
            numexpr = prod.IntExpr(number)
>>>>>>> 83a111722c2bfa0a77c1687112f108e7cb6e50b6
            op = self.peek()

            if op in ['PLUS', 'MINUS', 'DIV', 'MULT']:
                return self.infix(numexpr, op)
            else:
                return numexpr
        else:
<<<<<<< HEAD
            assert False, f"Syntax error {self.scanner.error()}"

    def name(self):
        name = self.match('NAME')
        return prod.NameExpr(name)

    def integer(self):
        number = self.match('INTEGER')
        return prod.IntExpr(number)

    def assign(self):
        self.skip('LET')
        nameexpr = self.name()
        self.skip('EQUAL')
        right = self.expression()
        return prod.AssignExpr(nameexpr, right)
=======
            assert False, "Syntax error %r" % start

    def assign(self, name):
        self.skip('EQUAL')
        right = self.expression()
        return prod.AssignExpr(name, right)
>>>>>>> 83a111722c2bfa0a77c1687112f108e7cb6e50b6

    def infix(self, left, op):
        """plus = expression PLUS expression"""
        self.match(op)
        right = self.expression()
        return prod.InfixExpr(left, op, right)

<<<<<<< HEAD
    def print(self):
        self.match('PRINT')
        expr = self.expression()
        return prod.PrintExpr(expr)

=======
>>>>>>> 83a111722c2bfa0a77c1687112f108e7cb6e50b6
class BasicWorld(object):

    def __init__(self, variables):
        self.variables = variables
        self.functions = {}

    def clone(self):
        """Sort of a lame way to implement scope."""
        temp = BasicWorld(self.variables.copy())
        temp.functions = self.functions
        return temp


def run(script):
    scanner = Scanner(TOKENS, script)
    parser = BasicParser(scanner)
    parse_tree = parser.parse()
    world = BasicWorld({})
    analyzer = BasicAnalyzer(parse_tree, world)
    prods = analyzer.analyze()
    for prod in prods:
<<<<<<< HEAD
        prod.interpret(world)
=======
        print(prod.interpret(world))
>>>>>>> 83a111722c2bfa0a77c1687112f108e7cb6e50b6

if __name__ == "__main__":
    _, script = sys.argv

    run(open(script).readlines())
