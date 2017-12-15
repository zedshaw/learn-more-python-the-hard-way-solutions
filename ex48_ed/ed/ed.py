import sys
import ed
from ed.scanner import Scanner
from ed.parser import EdParser

def process(line, buffer):
    scan = Scanner([line])
    ed_parser = EdParser(scan, buffer)
    parse_tree = ed_parser.parse()
 
class Buffer(object):
    def __init__(self, file_name=None):
        self.file_name = file_name

        if file_name:
            self.edit(file_name)
        else:
            self.lines = []

    def append(self, text, address=None):
        if address == None:
            # append at the end
            self.lines.append(text)
        else:
            # position it after the given line
            self.lines.insert(address, text)



    def change(self, start=None, end=None):
        pass

    def delete(self, start=None, end=None):
        pass

    def edit(self, file_name):
        self.lines = []
        self.read(file_name)
        self.file_name = file_name

    def file(self, file_name):
        self.file_name = file_name

    def glob(self, pattern, commands, start=1, end=None):
        pass

    def insert(self, address=None):
        pass

    def join(self, start=None, end=None):
        pass

    def mark(self, address=None):
        pass

    def move(self, start=None, end=None, to=None):
        pass

    def nprint(self, start, end):
        for i, line in enumerate(self.lines):
            print(f"{i}\t{line}")

    def print(self, start, end):
        start = start or 0
        end = end or len(self.lines)
        for line in self.lines[start:end]:
            print(line)

    def quit(self):
        sys.exit(0)

    def read(self, file_name, address=None):
        self.lines += open(file_name).readlines()

    def subst(self, pattern, replace, start=None, end=None):
        pass

    def write(self, file_name=None):
        file_name = file_name or self.file_name
        assert file_name, "Need a file name!"
        open(file_name, 'w').write("\n".join(self.lines))

    def undo(self):
        pass

    def line_count(self):
        return len(self.lines)
