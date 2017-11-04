import subprocess
import sys
import os


while True:
    line = input('> ')
    exec = line.strip().split(' ')
    status = subprocess.run(exec)

