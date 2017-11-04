import sys
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-f', '--foo', help='foo help')
# args = parser.parse_args()

_, tr_from, tr_to = sys.argv


for line in sys.stdin.readlines():
    print(line.replace(tr_from, tr_to), end="")

