import re
from calc.scanner import Scanner
from calc.parser import Parser
from calc.analyzer import CalcAnalyzer
from calc import productions as prod
import sys
import readline

TOKENS = [
(re.compile(r"^define"),                "DEFINE"),
(re.compile(r"^return"),                "RETURN"),
(re.compile(r"^print"),                "PRINT"),
(re.compile(r"^if"),                    "IF"),
(re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
(re.compile(r"^[0-9]+"),                 "INTEGER"),
(re.compile(r"^\{"),                    "LBRACE"),
(re.compile(r"^\}"),                    "RBRACE"),
(re.compile(r"^\("),                     "LPAREN"),
(re.compile(r"^\)"),                     "RPAREN"),
(re.compile(r"^\="),                     "EQUAL"),
(re.compile(r"^\+"),                     "PLUS"),
(re.compile(r"^\-"),                     "MINUS"),
(re.compile(r"^\*"),                     "MULT"),
(re.compile(r"^/"),                     "DIV"),
(re.compile(r"^\s+"),                     "SPACE"),
(re.compile(r"^,"),                      "COMMA"),
]

class CalcParser(Parser):

    def root(self):
        """root = *(func_def | if | print | expression)"""
        first = self.peek()

        if first == 'DEFINE':
            return self.function_definition()
        elif first == 'IF':
            return self.if_statement()
        elif first == 'PRINT':
            return self.print_statement()
        else:
            return self.expression()

    def print_statement(self):
        pname = self.match('PRINT')
        expr = self.parameters()
        return prod.FuncCall(pname, expr)

    def function_call(self, name):
        """funccall = name LPAREN params RPAREN"""
        params = self.parameters()
        return prod.FuncCall(name, params)

    def function_definition(self):
        self.skip('DEFINE')
        name = self.match('NAME')
        params = self.parameters()
        self.skip('LBRACE')
        body = self.function_body()
        return prod.FuncDef(name, params, body)

    def if_statement(self):
        self.skip('IF', 'LPAREN')
        expr = self.expression()
        self.skip('RPAREN')

    def function_body(self):
        start = self.peek()
        body = []

        while start != 'RBRACE':
            # just call root for now but that will allow defining a function
            # inside this function which isn't right
            body.append(self.root())
            start = self.peek()

        self.skip('RBRACE')
        return body

    def parameters(self):
        """params = expression *(COMMA expression)"""
        params = []

        self.skip('LPAREN')
        start = self.peek()
        while start != 'RPAREN':
            params.append(self.expression())
            start = self.peek()
            if start != 'RPAREN':
                assert self.skip('COMMA'), self.syntax_error("Invalid parameter syntax.")
        self.skip('RPAREN')

        return prod.Parameters(params)


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
            elif op == 'LPAREN':
                return self.function_call(name)
            else:
                return nameexpr
        elif start == 'RETURN':
            # for now we can be expression based and just ignore the return
            self.skip('RETURN')
            return self.expression()
        elif start == 'INTEGER':
            number = self.match('INTEGER')
            numexpr = prod.IntExpr(number)
            op = self.peek()

            if op in ['PLUS', 'MINUS', 'DIV', 'MULT']:
                return self.infix(numexpr, op)
            else:
                return numexpr
        else:
            assert False, self.syntax_error("Invalid syntax in EXPRESSION")

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
        self.functions = {'print': prod.PrintFuncDef()}

    def clone(self):
        """Sort of a lame way to implement scope."""
        temp = CalcWorld(self.variables.copy())
        temp.functions = self.functions
        return temp


def run(script):
    scanner = Scanner(TOKENS, script)
    parser = CalcParser(scanner)
    parse_tree = parser.parse()
    print_def = prod.PrintFuncDef()
    world = CalcWorld({})
    analyzer = CalcAnalyzer(parse_tree, world)
    prods = analyzer.analyze()
    for p in prods:
        p.interpret(world)

def shell():
    world = CalcWorld({})
    print_def = prod.PrintFuncDef()

    while True:
        try:
            line = input("> ")
        except EOFError:
            print()
            sys.exit(0)

        scanner = Scanner(TOKENS, [line])
        parser = CalcParser(scanner)
        parse_tree = parser.parse()
        analyzer = CalcAnalyzer(parse_tree, world)
        prods = analyzer.analyze()
        for p in prods:
            val = p.interpret(world)
            if val: print(val)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        _, script = sys.argv
        run(open(script).readlines())
    else:
        shell()

