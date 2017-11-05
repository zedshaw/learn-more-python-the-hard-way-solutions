import difflib
import sys

def create_diff(style, left_lines, right_lines, fromfile="", tofile=""):
    if style == "n":
        return difflib.ndiff(left_lines, right_lines)
    elif style == "c":
        return difflib.context_diff(left_lines, right_lines,
                                    fromfile=fromfile, tofile=tofile)
    elif style == "u":
        # default to unified diff
        return difflib.unified_diff(left_lines, right_lines,
                                    fromfile=fromfile, tofile=tofile)
    else:
        assert False, "Invalid diff style."

def main(style, left, right, outfile):
    left_lines = open(left).readlines()
    right_lines = open(right).readlines()
    diff = create_diff(style, left_lines, right_lines, fromfile=left, tofile=right)
    outfile.writelines(diff)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        assert sys.argv[1][0] == '-', "Argument error."
        _, diff_style, left, right = sys.argv
        main(diff_style[1], left, right, sys.stdout)
    else:
        _, left, right = sys.argv
        main('u', left, right, sys.stdout)

