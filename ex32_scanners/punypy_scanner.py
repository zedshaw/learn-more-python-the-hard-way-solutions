

class Scanner(object):

    def __init__(self, regex, code):
        self.regex_list = regex
        self.code = code
        self.tokens = self.scan(code)


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

        for line in code:
            i = 0
            while i < len(line):
                token, string, end = self.match_regex(i, line)
                assert token, "Failed to match line %s" % string
                if token:
                    i += end
                    self.script.append((token, string, i, end)) 

        return self.script

    def done(self):
        return len(self.tokens) == 0
