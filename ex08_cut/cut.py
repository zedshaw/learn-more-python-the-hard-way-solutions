import sys

_, delim, fields = sys.argv
split_at = [int(x) for x in fields.split(',')]

while True:
    try:
        line = input()
        cuts = line.split(delim)
        for i in split_at:
            print(f"{cuts[i]} ", end="")
        print()

    except EOFError:
        sys.exit(0)
    except IndexError:
        pass


