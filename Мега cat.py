import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--count", action="store_true")
parser.add_argument("--num", action="store_true")
parser.add_argument("--sort", action="store_true")
parser.add_argument("file", nargs=1, type=str)

args = parser.parse_args()
count = args.count
num = args.num
sort = args.sort
file = args.file

try:
    with open(file[0], mode="r") as source:
        lines = source.readlines()
        data = lines

    if sort:
        data = sorted(data)

    for i, elem in enumerate(data):
        if num:
            print(i, end=" ")
        print(elem.rstrip())

    if count:
        print(f"rows count: {len(lines)}")

    source.close()
except Exception:
    print("ERROR")
