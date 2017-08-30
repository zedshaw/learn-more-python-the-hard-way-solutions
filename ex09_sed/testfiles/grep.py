import re
import sys
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('pattern', type=str, nargs=1) 
    parser.add_argument('start', type=str, nargs=1) 
    parser.add_argument('-r', action='store_true')

    return parser.parse_args()

def find_in_file(name, pattern):
    try:
        lines = open(name).readlines()
    except UnicodeDecodeError:
        print(f"Binary file {name} matches.")
        return

    expr = re.compile(pattern)

    for line in lines:
        if expr.search(line):
            print(line, end="")

args = parse_args()
if args.r:
    start_path = Path(args.start[0])
    for f in start_path.rglob("*"):
        if f.is_file():
            find_in_file(f, args.pattern[0])
else:
    find_in_file(args.start[0], args.pattern[0])
