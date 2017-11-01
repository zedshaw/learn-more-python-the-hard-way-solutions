from scanner import *
from pprint import pprint

def root(tokens):
    """root = *(funccal / funcdef)"""
    first = peek(tokens)

    if first == 'DEF':
        return function_definition(tokens)
    elif first == 'NAME':
        name = match(tokens, 'NAME')
        second = peek(tokens)

        if second == 'LPAREN':
            return function_call(tokens, name)
        else:
            assert False, "Not a FUNCDEF or FUNCCALL"

def function_definition(tokens):
    """
    funcdef = DEF name LPAREN params RPAREN COLON body
    I ignore body for this example 'cause that's hard.
    I mean, so you can learn how to do it.
    """
    skip(tokens) # discard def
    name = match(tokens, 'NAME')
    match(tokens, 'LPAREN')
    params = parameters(tokens)
    match(tokens, 'RPAREN')
    match(tokens, 'COLON')
    return {'type': 'FUNCDEF', 'name': name, 'params': params}

def parameters(tokens):
    """params = expression *(COMMA expression)"""
    params = []
    start = peek(tokens)
    while start != 'RPAREN':
        params.append(expression(tokens))
        start = peek(tokens)
        if start != 'RPAREN':
            assert match(tokens, 'COMMA')
    return params

def function_call(tokens, name):
    """funccall = name LPAREN params RPAREN"""
    match(tokens, 'LPAREN')
    params = parameters(tokens)
    match(tokens, 'RPAREN')
    return {'type': 'FUNCCALL', 'name': name, 'params': params}

def expression(tokens):
    """expression = name / plus / integer"""
    start = peek(tokens)

    if start == 'NAME':
        name = match(tokens, 'NAME')
        if peek(tokens) == 'PLUS':
            return plus(tokens, name)
        else:
            return name
    elif start == 'INTEGER':
        number = match(tokens, 'INTEGER')
        if peek(tokens) == 'PLUS':
            return plus(tokens, number)
        else:
            return number
    else:
        assert False, "Syntax error %r" % start

def plus(tokens, left):
    """plus = expression PLUS expression"""
    match(tokens, 'PLUS')
    right = expression(tokens)
    return {'type': 'PLUS', 'left': left, 'right': right}


def main(tokens):
    results = []
    while tokens:
        results.append(root(tokens))
    return results

parsed = main(scan(code))
pprint(parsed)
