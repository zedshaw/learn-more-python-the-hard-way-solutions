import sys
from scanner import Scanner
from parser import EdParser

def process(line, buffer):
    scan = Scanner(line)
    ed_parser = EdParser(scan, buffer)
    parse_tree = ed_parser.parse()
 
