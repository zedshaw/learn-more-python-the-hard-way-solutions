#!/usr/bin/env python

import subprocess
import sys

command = sys.argv[1:]

for line in sys.stdin.readlines():
    exec = command + [line.strip()]
    status = subprocess.run(exec)
