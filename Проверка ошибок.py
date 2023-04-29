import argparse

parser = argparse.ArgumentParser()
parser.add_argument('message', nargs='*', type=str)

arg = parser.parse_args()
message = arg.message


def print_error(mes='message'):
    print('ERROR:', mes + '!!')


if message:
    print('Welcome to my program')
    print_error(' '.join(message))
