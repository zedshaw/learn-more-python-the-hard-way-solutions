#!/usr/bin/env python

import subprocess
import sys

command = sys.argv[1:]
if command[0] == '-I':
    _ = command.pop(0)
    replace = command.pop(0)
    print("Command: ", command)
else:
    replace = None

for line in sys.stdin.readlines():
    if replace:
        l = line.strip()
        exec = [c.replace(replace, l) for c in command] 
    else:
        exec = command + [line.strip()]

    status = subprocess.run(exec)

