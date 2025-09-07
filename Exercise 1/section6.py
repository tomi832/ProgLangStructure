def square(x: int) -> int:
    return x * x

def twice(x: int) -> int:
    return 2 * x

def opposite(x: int) -> int:
    return -x

def absolute(x: int) -> int:
    return abs(x)

def increment(x: int) -> int:
    return x + 1

def is_even(x: int) -> bool:
    return x % 2 == 0

unaryFunctions = [
    square, twice, opposite, absolute, increment, is_even
]

"""
applying all of the funcs to each value in the list.
I've used tuples since they are immutable and slightly more efficient than lists, better for FP
As the more immutable data structures we use, the more FP-like our code is.
"""
def apply_all(funcs: list, values: list) -> dict:
    names = tuple(map(lambda f: f.__name__, funcs))
    return dict(zip(names, tuple(map(lambda f: tuple(map(lambda v: f(v), values)), funcs))))

# for testing, not part of the assignment
#print(apply_all(unaryFunctions, [1, -2, 3, -4, 5]))