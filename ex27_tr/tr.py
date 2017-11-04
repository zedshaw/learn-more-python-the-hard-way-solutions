#!/usr/bin/env python
import sys

def translate(from_c, to_c, in_string):
    return in_string.replace(from_c, to_c)

def main(args, in_string):
    print(">>>> args", args)
    if args[0] == '-t':
        # need to truncate first to len of last
        to_c = args[2]
        from_c = args[1][:len(to_c)]
    else:
        from_c = args[0]
        to_c = args[1]
    print("from_c", from_c, "to_c", to_c)    
    return translate(from_c, to_c, in_string)

if __name__ == "__main__":
    print(main(sys.argv[1:], sys.stdin.read()))

