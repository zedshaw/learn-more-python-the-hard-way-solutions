import sys

lines = []

if len(sys.argv) > 1:
    for file_name in sys.argv[1:]:
        lines += [line for line in open(file_name).readlines() if len(line) > 20]
else:
    while True:
        try:
            line = input() + "\n"
            lines.append(line)
        except EOFError:
            break

print("".join(sorted(lines)), end="")
