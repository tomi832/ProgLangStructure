from functools import reduce
from math import factorial

def powers_list(max_power):
    return map(lambda power: lambda x: x**power, range(max_power))

def taylor_generator(x):
    n = 1
    while True:
        powers = tuple(powers_list(n))
        yield reduce(lambda acc, b: powers[b](x)/factorial(b) + acc, range(n), 0)
        n += 1

def main():
    taylor_gen = taylor_generator(2)
    for _ in range(8):
        print(next(taylor_gen))


if __name__ == "__main__":
    main()