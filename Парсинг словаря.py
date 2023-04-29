import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sort", action="store_true")
parser.add_argument("keys_and_values", nargs='*', type=str)

args = parser.parse_args()
sort = args.sort
keys_and_values = args.keys_and_values

res = {}

for elem in keys_and_values:
    temp_elem = elem.split('=')
    res[temp_elem[0]] = temp_elem[1]

if sort:
    res = dict(sorted(res.items()))

for elem in res:
    print(f"Key: {elem} Value: {res[elem]}")
