import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')

data = parser.parse_args()

if not data.arg:
    print('no args')
else:
    [print(x) for x in data.arg]
