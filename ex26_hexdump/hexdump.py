#!/usr/bin/env python

def reshape(data, n):
    results = []
    while data:
        results.append(data[:n])
        del data[:n]

    return results

def format_bytes(inbytes):
    byte_codes = inbytes.encode("utf-8")
    shaped = reshape([b for b in byte_codes], 16)
    return shaped

def format(infile):
    data = open(infile).read()
    formatted = format_bytes(data)
    count = 0
    for row in formatted:
        print(f"{count:010x} ", end="")
        print(" ".join(f"{x:02x}" for x in row))
        count += len(row)

if __name__ == "__main__":
    import sys
    format(sys.argv[1])
