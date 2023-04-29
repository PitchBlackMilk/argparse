import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', type=int, default=50)
parser.add_argument('--cars', type=int, default=50)
parser.add_argument('--movie', choices=['melodrama', 'football', 'other'], default='other')

args = parser.parse_args()
movie_list = {'melodrama': 0, 'football': 100, 'other': 50}


barbie = args.barbie if 0 <= args.barbie <= 100 else 50
cars = args.cars if 0 <= args.cars <= 100 else 50
movie = movie_list[args.movie]

boy = int((100 - barbie + cars + movie) / 3)
girl = 100 - boy

print(f'boy: {boy}')
print(f'girl: {girl}')

