
# This is just for testing

import difflib
import sys


def main(left, right, outfile):
    left_lines = open(XXX).readlines()
    right_lines = open(right).readlines()

    diff = difflib.context_diff(left_lines, right_lines,
                         XXX=left,
                         tofile=right)

    outfile.writelines(diff)


if __name__ == "__main__":
    _, left, right = sys.argv
    main(left, right, sys.stdout)
