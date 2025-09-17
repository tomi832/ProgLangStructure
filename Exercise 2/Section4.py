from functools import reduce
from math import factorial


def power_function(power):
    return lambda x: x**power


def powers_list(max_power):
    return map(power_function, range(max_power))


def taylor_approx(x, n):
    powers = tuple(powers_list(n))
    return reduce(lambda acc, b: powers[b](x)/factorial(b) + acc, range(n + 1), 0)

if __name__ == "__main__":
    print("Enter number of powers:")
    n = int(input())
    powers_map = powers_list(n)  # Creates map object with power functions
    print("Enter base:")
    base = int(input())
    print(type(powers_map))  # <class 'map'>
    print(tuple(map(lambda f: f(base), powers_map)))
