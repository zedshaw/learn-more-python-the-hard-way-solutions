import re

def parse_script(script):
    if script[0] == "s":
        return ('s', script.split('/')[1:3])
    elif script[0] == "r":
        return ('r', script.split(' ')[1:])
    else:
        print("Error, only s supported")
        sys.exit(1)

def do_s(file_name, pattern, replace):
    with open(file_name) as f:
        for line in f.readlines():
            fixed = re.sub(pattern, replace, line)
            print(fixed, end="")

def do_r(file_name, in_file_name):
    contents = open(in_file_name).read()

    with open(file_name) as f:
        for line in f.readlines():
            print(line, contents, end='')

def apply_script(command, file_name, args):
    if command == "s":
        do_s(file_name, *args)
    elif command == "r":
        do_r(file_name, *args)
    else:
        print("Not supported.")
        sys.exit(1)

def sed(script, files):
    command, args = parse_script(script)
    for file_name in files:
        apply_script(command, file_name, args)

def print_uniq_lines(file_list):
    all_lines = set()

    for f in file_list:
        all_lines |= set(f.readlines())
        
    print("".join(all_lines))

