import sys
import tools

script = sys.argv[1]
files = sys.argv[2:]

tools.sed(script, files)
