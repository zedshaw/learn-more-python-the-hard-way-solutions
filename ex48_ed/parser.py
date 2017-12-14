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


class EdParser(Parser):

    def __init__(self, scanner, buffer):
        super().__init__(scanner)
        self.buffer = buffer
        self.cur_line = 0

    def root(self):
        start = self.peek()

        if start == 'PRINT':
            self.print(self.cur_line)
        elif start == 'INTEGER':
            # this is an address
            self.address()
        elif start == 'COMMA':
            self.range()
        else:
            assert False, "Not supported."

    def address(self):
        # need to handle the range here
        addr = self.match('INTEGER')
        addr_n = addr[1]
        assert addr_n > 0 and addr_n < len(self.buffer)
        self.cur_line = addr_n
            

    def range(self):
        # right now only whole buffer
        self.match('COMMA')
        self.print(0, end=len(self.buffer))

    def print(self, start, end=None):
        self.match('PRINT')
        if end:
            print("\n".join(self.buffer[start:end]))
        else:
            print(self.buffer[start])

