from functools import reduce

ls = list(range(1, 1001))

ls_even = [ x for x in ls if x % 2 == 0 ]
ls_odd = [ x for x in ls if x % 2 != 0 ]

func1 = lambda i, even_ls: reduce(
    lambda acc, x: acc + [x * acc[-1]],
    even_ls[2:i],                 # start from the 3rd element onward
    [even_ls[0] * even_ls[1]]     # seed with first*second
)

func2 = lambda odd_ls: [odd_ls[i] / 2 + 2 + odd_ls[i + 1] for i in range(len(odd_ls) - 1)]

# chose 100 as a random i for func1, since it's supposed to get a number and the exercise pdf didn't
# tell us to use a specific one
def super_func(f1, f2, even_ls, odd_ls):
    return sum(f1(100, even_ls)) + sum(f2(odd_ls))
