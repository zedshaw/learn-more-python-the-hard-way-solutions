import readline
import sys
from ed import ed

buffer = ed.Buffer()

while True:
    try:
        line = input("> ")
        ed.process(line, buffer)
    except EOFError: 
        print()
        sys.exit(0)
