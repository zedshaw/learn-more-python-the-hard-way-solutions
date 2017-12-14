import sys
import ed

_, infile = sys.argv

buffer = open(infile).readline()

while True:
    try:
        command = input("> ")
    except EOFError: 
        print()
        sys.exit(0)

    
