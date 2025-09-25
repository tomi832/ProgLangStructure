# normal recursion
def thousand_tuple():
    return recTuple(1, ())

def recTuple(i, tup):
    if i > 1000:
        return tup
    return recTuple(i + 1, tup + (i,))

###################
def thousand_tuple_tail():
    return recTuple_tail(1, ())


def recTuple_tail(i, accumulative_tuple):
    if i > 1000:
        return accumulative_tuple
    return recTuple_tail(i + 1, accumulative_tuple + (i,))


if __name__ == "__main__":
    print(thousand_tuple_tail())