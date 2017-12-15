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
        elif start == 'NPRINT':
            self.nprint()
        elif start == 'APPEND':
            self.append()
        elif start == 'FILE':
            self.file()
        elif start == 'WRITE':
            self.write()
        elif start == 'QUIT':
            self.buffer.quit()
        elif start == 'SUBST':
            self.subst()
        elif start == 'INTEGER':
            # this is an address
            self.address()
        elif start == 'JOIN':
            self.join()
        elif start == 'COMMA':
            self.address_range()
        else:
            assert False, f"Not supported  {self.match(start)}"

    def address(self):
        # need to handle the range here
        addr = self.match('INTEGER')
        addr_n = int(addr[1])
        self.cur_line = addr_n
        if self.peek() == 'COMMA':
            self.address_range()
            
    def address_range(self):
        # right now only whole buffer
        self.match('COMMA')
        if self.peek() == 'INTEGER':
            addr = self.match('INTEGER')
            addr_n = int(addr[1])
            self.range = (self.cur_line, addr_n)
        else:
            self.range = (0, self.buffer.line_count())


    def calc_range(self):
        if self.range:
            return self.range
        else:
            return self.cur_line, self.cur_line + 1

    def print(self):
        self.match('PRINT')
        self.buffer.print(*self.calc_range())

    def nprint(self):
        self.match('NPRINT')
        self.buffer.nprint(*self.calc_range())

    def append(self):
        self.match('APPEND')
        line = input()
        while line != '.':
            self.buffer.append(line, address=self.cur_line)
            self.cur_line += 1
            line = input()

    def write(self):
        self.match('WRITE')
        self.buffer.write()

    def file(self):
        self.match('FILE')
        file_name = self.match('FILE_NAME')
        self.buffer.file(file_name[1])

    def join(self):
        self.match('JOIN')
        self.buffer.join(*self.calc_range())

    def subst(self):
        self.match('SUBST')
        pat_tok = self.match('PATTERN')[1]
        _, pattern, replace, _ = pat_tok.split('/')
        self.buffer.subst(pattern, replace)

