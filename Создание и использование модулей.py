import argparse


def count_lines(file):
    try:
        with open(file, mode='r') as file:
            return len(file.readlines())
    except Exception:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    arg = parser.parse_args()
    file = arg.file
    print(count_lines(file))

