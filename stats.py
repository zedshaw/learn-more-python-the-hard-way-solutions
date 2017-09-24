#!/usr/bin/env python

import numpy
import sys
import bokeh
import os

command = sys.argv[1]
name = sys.argv[2]
args = sys.argv[3:]

SAVE_DIR = ".morepystats"


if command == "add":
    # add a new stat
    file_name = f"{SAVE_DIR}/{name}.npy"
    assert os.path.exists(SAVE_DIR), f"No save dir {SAVE_DIR}. In the right place?"
    
    if os.path.exists(file_name):
        arg_data = numpy.array([[float(a) for a in args]])
        data = numpy.load(file_name)
        new_data = numpy.concatenate((data, arg_data), axis=0)
    else:
        new_data = numpy.array([[float(a) for a in args]])
    numpy.save(file_name, new_data)

elif command == "init":
    # init a new set of stats
    if not os.path.exists(SAVE_DIR): os.mkdir(SAVE_DIR)

elif command == "stats":
    # show the stats so far
    file_name = f"{SAVE_DIR}/{name}.npy"
    data = numpy.load(file_name)
    mean = numpy.mean(data, axis=0)
    stddev = numpy.std(data, axis=0)
    q25, q50, q75 = quartile = numpy.percentile(data, [25, 50, 75], axis=0)
    for i in range(0, len(q25)):
        print("---")
        print(f"mean\t{mean[i]}\nstddev\t{stddev[i]}")
        print(f"q\t{q25[i]} {q50[i]} {q75[i]}\nIQR\t{q75[i] - q25[i]}")

elif command == "graph":
    # graph the runchart for the stat
    pass
else:
    print("USAGE: add stats or graph commands.")

