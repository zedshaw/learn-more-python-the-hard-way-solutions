import re
from punypy.parser import Parser

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
                assert False, "Not a FUNCDEF or FUNCCALL"

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
        return {'type': 'FUNCDEF', 'name': name, 'params': params}

    def parameters(self):
        """params = expression *(COMMA expression)"""
        params = []
        start = self.peek()
        while start != 'RPAREN':
            params.append(self.expression())
            start = self.peek()
            if start != 'RPAREN':
                assert self.skip('COMMA')
        return params

    def function_call(self, name):
        """funccall = name LPAREN params RPAREN"""
        self.match('LPAREN')
        params = self.parameters()
        self.match('RPAREN')
        return {'type': 'FUNCCALL', 'name': name, 'params': params}

    def expression(self):
        """expression = name / plus / integer"""
        start = self.peek()

        if start == 'NAME':
            name = self.match('NAME')
            if self.peek() == 'PLUS':
                return self.plus(name)
            else:
                return name
        elif start == 'INTEGER':
            number = self.match('INTEGER')
            if self.peek() == 'PLUS':
                return self.plus(number)
            else:
                return number
        else:
            assert False, "Syntax error %r" % start

    def plus(self, left):
        """plus = expression PLUS expression"""
        self.match('PLUS')
        right = self.expression()
        return {'type': 'PLUS', 'left': left, 'right': right}


