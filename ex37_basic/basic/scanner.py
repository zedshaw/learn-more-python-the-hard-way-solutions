

class Scanner(object):

    def __init__(self, regex, code):
        self.regex_list = regex
        self.code = code
        self.tokens = self.scan(code)

    def ignore_ws(self):
        while self.tokens and self.tokens[0][0] == 'SPACE':
            self.tokens.pop(0)

    def match(self, token_id):
        if token_id != 'SPACE':
            self.ignore_ws()

        if self.tokens[0][0] == token_id:
            return self.tokens.pop(0)
        else:
            return ['ERROR', 'error']

    def peek(self):
        self.ignore_ws()
        if self.tokens:
            return self.tokens[0][0]
        else:
            return ['END', 'end']

    def error(self):
        token, string, line_no, i, end = self.tokens[0]
        
        return f"ERROR: {token}{string} at line {line_no}@{i}"

    def skip(self, *what):
        for x in what:
            if x != 'SPACE': self.ignore_ws()

            tok = self.tokens[0]
            if tok[0] != x:
                return False
            else:
                self.tokens.pop(0)

        return True


    def match_regex(self, i, line):
        start = line[i:]
        for regex, token in self.regex_list:
            tok = regex.match(start)
            if tok:
                begin, end = tok.span()
                return token, start[:end], end
        return None, start, None


    def scan(self, code):
        self.script = []
        line_no = 0

        for line in code:
            i = 0
            line = line.rstrip()
            line_no += 1
            while i < len(line):
                token, string, end = self.match_regex(i, line)
                assert token, "Failed to match line %s" % string
                if token:
                    i += end
                    self.script.append((token, string, line_no, i, end))

        return self.script

    def done(self):
        return len(self.tokens) == 0
