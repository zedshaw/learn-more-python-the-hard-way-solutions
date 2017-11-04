import subprocess
import sys
import os

def parse(line):
    return [x.strip() for x in line.split(' ') if x]

def interpret(exec):
    if exec[0] == 'exit':
        sys.exit(0)
    elif exec[0] == 'cd':
        if len(exec) == 2:
            os.chdir(exec[1])
        else:
            print("Error: cd DIR")
    else:
        subprocess.run(exec)

def run(line):
    exec = parse(line)

    if exec:
        return interpret(exec)
    else:
        return None

def main():
    while True:
        try:
            line = input('> ')
            # need to find out if we should process this
            status = run(line)
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == "__main__":
    main()
