from functools import reduce

def add_3_dicts(d1, d2, d3):
    items = (list(d1.items()) + list(d2.items()) + list(d3.items()))
    return reduce(
        lambda acc, x: { **acc, x[0]: tuple(dict.fromkeys(acc.get(x[0], ()) + (x[1],)))},
        items,
        {}
    )
    # from what I found online, fromkeys removes duplicates while preserving order,
    # which would be better than set which doesn't preserve order, though we weren't tasked to do so