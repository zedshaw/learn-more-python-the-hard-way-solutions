from pprint import pprint


class Parser(object):

    def __init__(self, scanner):
        self.scanner = scanner

    def match(self, token_id):
        return self.scanner.match(token_id)

    def peek(self):
        return self.scanner.peek()

    def skip(self, *what):
        return self.scanner.skip(*what)

    def root(self):
        pass

    def parse(self):
        results = []
        while not self.scanner.done():
            results.append(self.root())
        return results

    def syntax_error(self, message):
        return f"{message}: {self.scanner.tokens[:10]}"



