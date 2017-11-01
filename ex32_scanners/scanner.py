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


def ignore_ws(tokens):
    while tokens[0][0] == 'INDENT':
        tokens.pop(0)

def match(tokens, token_id):
    if token_id != 'INDENT':
        ignore_ws(tokens)

    if tokens[0][0] == token_id:
        return tokens.pop(0)
    else:
        assert False, "Expected %r got %r" % (token_id, tokens[0])

def peek(tokens):
    ignore_ws(tokens)
    return tokens[0][0]

def skip(tokens):
    ignore_ws(tokens)
    tokens.pop(0)


def match_regex(i, line):
    start = line[i:]
    for regex, token in TOKENS:
        tok = regex.match(start)
        if tok:
            begin, end = tok.span()
            return token, start[:end], end
    return None, start, None


def scan(code):
    script = []

    for line in code:
        i = 0
        while i < len(line):
            token, string, end = match_regex(i, line)
            assert token, "Failed to match line %s" % string
            if token:
                i += end
                script.append((token, string, i, end)) 

    return script
