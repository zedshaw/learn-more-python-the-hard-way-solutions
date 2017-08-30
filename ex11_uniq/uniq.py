#!/usr/bin/env python3.6

import sys

def print_uniq_lines(file_list):
    all_lines = set()

    for f in file_list:
        all_lines |= set(f.readlines())
        
    print("".join(all_lines))

if len(sys.argv) > 1:
    print_uniq_lines(open(f) for f in sys.argv[1:])
else:
    print_uniq_lines([sys.stdin])

