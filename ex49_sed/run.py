import readline
import sys
import argparse
from ed import ed

parser = argparse.ArgumentParser()
parser.add_argument("infile", type=str, help="Input file.")
parser.add_argument("-e", type=str, help="The script.")
parser.add_argument("-f", type=str, help="A file script.", default=None)
parser.add_argument("-n", action="store_true")
args = parser.parse_args()

buffer = ed.Buffer()
buffer.edit(args.infile)

if args.e:
    ed.process(args.e, buffer)
elif args.f:
    lines = (x.strip() for x in open(args.f).readlines())
    for line in lines:
        ed.process(line, buffer)

print("\n".join(buffer.lines))
