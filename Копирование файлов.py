import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--upper', action='store_true')
parser.add_argument('--lines', nargs=1, type=int)
parser.add_argument('files', nargs='*', type=str)


args = parser.parse_args()
upper = args.upper
lines_amount = args.lines
files = args.files

with open(files[0], mode='r') as source:
    lines = source.readlines()
    if upper:
        lines = list(map(lambda line: line.upper(), lines))
    with open(files[1], mode='w') as result:
        if lines_amount:
            result.writelines(lines[:lines_amount[0]])
        else:
            result.writelines(lines)
source.close()
result.close()

