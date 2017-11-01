#!/usr/bin/env python

import numpy
import sys
from bokeh import plotting
import os

command = sys.argv[1]
if command != "init":
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
    assert os.path.exists(SAVE_DIR), f"No save dir {SAVE_DIR}. In the right place?"

    # show the stats so far
    file_name = f"{SAVE_DIR}/{name}.npy"
    data = numpy.load(file_name)
    mean = numpy.mean(data, axis=0)
    stddev = numpy.std(data, axis=0)
    q25, q50, q75 = quartile = numpy.percentile(data, [25, 50, 75], axis=0)
    for i in range(0, len(q25)):
        print("---")
        print(f"mean\t{mean[i]}\nstddev\t{stddev[i]}")
        print(f"sd+/-1\t{mean[i] - stddev[i]}, {mean[i] + stddev[i]}")
        print(f"sd+/-2\t{mean[i] - 2 * stddev[i]}, {mean[i] + 2 * stddev[i]}")
        print(f"q\t{q25[i]} {q50[i]} {q75[i]}\nIQR\t{q75[i] - q25[i]}")

elif command == "graph":
    out_dir = len(args) > 0 and args[0] or SAVE_DIR
    assert os.path.exists(out_dir), f"No save dir {out_dir}. In the right place?"
    plotting.output_file(f"{out_dir}/{name}.html")
    file_name = f"{SAVE_DIR}/{name}.npy"
    data = numpy.load(file_name)

    p = plotting.figure(title=f"stats for {name}", x_axis_label='x',
                     y_axis_label='y')

    for i in range(len(data[0,:])):
        row = data[:,i]
        p.line(range(0, len(row)), row, legend=f"S{i}", line_width=2)
        means = [numpy.mean(row)] * len(row)
        p.line(range(0, len(row)), means, legend=f"mean{i}", line_width=1, color="green")

        sdplus1 = [numpy.mean(row) + numpy.std(row)] * len(row)
        p.line(range(0, len(row)), sdplus1, legend=f"+-sd{i}", line_width=1, color="orange")

        sdminus1 = [numpy.mean(row) - numpy.std(row)] * len(row)
        p.line(range(0, len(row)), sdminus1, legend=f"+-sd{i}", line_width=1, color="orange")

        sdplus2 = [numpy.mean(row) + numpy.std(row) * 2] * len(row)
        p.line(range(0, len(row)), sdplus2, legend=f"+-sd{i}", line_width=1, color="red")

        sdminus2 = [numpy.mean(row) - numpy.std(row) * 2] * len(row)
        p.line(range(0, len(row)), sdminus2, legend=f"+-sd{i}", line_width=1, color="red")


    plotting.show(p)

else:
    print("USAGE: add stats or graph commands.")

