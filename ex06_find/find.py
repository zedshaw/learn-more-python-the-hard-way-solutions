from pathlib import Path
import sys
import argparse

def name_find(start, args):
    for f in start.rglob(args.name):
        print(f)

def type_find(start, args):
    if args.type not in ['d','f']:
        print(f"Unknown type: {args.type}")
        sys.exit(1)

    for f in start.rglob(args.name or "*"):
        if args.type == "d" and f.is_dir():
            print(f)
        elif args.type == "f" and f.is_file():
            print(f)


def find_files(args):
    start_path = Path(args.start[0])
    
    if args.name and not args.type:
        name_find(start_path, args)
    elif args.type:
        type_find(start_path, args)
    else:
        print("You need either --name or --type")
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('start', type=str, nargs=1) 
    parser.add_argument('--name', type=str)
    parser.add_argument('--type' , type=str)

    return parser.parse_args()

find_files(parse_args())

