import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integers', nargs='*', type=str)


args = parser.parse_args()
numbers = args.integers


class NoneError(Exception):
    pass


class TooFew(Exception):
    pass


class TooMany(Exception):
    pass


def summa(num):
    try:
        if not len(num):
            raise NoneError
        if len(num) == 1 or any([not int(i) for i in num]):
            raise TooFew
        elif len(num) > 2:
            raise TooMany

        return int(num[0]) + int(num[1])
    except NoneError:
        return 'NO PARAMS'
    except TooFew:
        return 'TOO FEW PARAMS'
    except TooMany:
        return 'TOO MANY PARAMS'
    except ValueError:
        return 'ValueError'


try:
    print(summa(numbers))
except Exception as error:
    print(error.__class__.__name__)