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

def match(i, line):
    start = line[i:]
    for regex, token in TOKENS:
        match = regex.match(start)
        if match:
            begin, end = match.span()
            return token, start[:end], end
    return None, start, None

script = []

for line in code:
    i = 0
    while i < len(line):
        token, string, end = match(i, line)
        assert token, "Failed to match line %s" % string
        if token:
            i += end
            script.append((token, string, i, end)) 

print(script)
