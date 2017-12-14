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
        self.range = None
        self.cur_line = 0

    def root(self):
        start = self.peek()

        if start == 'PRINT':
            self.print()
        elif start == 'APPEND':
            self.append()
        elif start == 'INTEGER':
            # this is an address
            self.address()
        elif start == 'COMMA':
            self.address_range()
        else:
            assert False, "Not supported."

    def address(self):
        # need to handle the range here
        addr = self.match('INTEGER')
        addr_n = int(addr[1])
        self.cur_line = addr_n
            
    def address_range(self):
        # right now only whole buffer
        self.match('COMMA')
        self.range = (0, self.buffer.line_count())

    def print(self):
        self.match('PRINT')
        if self.range:
            start, end = self.range
        else:
            start = self.cur_line
            end = self.cur_line + 1

        self.buffer.print(start, end)

    def append(self):
        self.match('APPEND')
        line = input()
        while line != '.':
            self.cur_line += 1
            self.buffer.append(line)
            line = input()

