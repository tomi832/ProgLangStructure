import time

def lazy_eval():
    for i in range(10000):
        yield i

def non_lazy_eval():
    return [x for x in range(10000)]


def main():
    time_start_eval = time.time()
    # it is not super clear what the assignment wants. it asks for a list of 10000 elements, but also to use lazy evaluation.
    # so i did use a generator and then convert it to a list, but now it takes even more time then the non-lazy version,
    # and takes the same amount of space in memory (obviously, since both are lists now).
    # TODO: Redo the comments
    full_list1 = lazy_eval()
    time_end_eval = time.time()
    print("Lazy evaluation took:", time_end_eval - time_start_eval, "seconds")

    time_start_non_eval = time.time()
    full_list2 = non_lazy_eval()
    time_end_non_eval = time.time()
    print("Non-lazy evaluation took:", time_end_non_eval - time_start_non_eval, "seconds")
    print("full_list1 size in memory:", full_list1 .__sizeof__(), "bytes")
    print("full_list2 size in memory:", full_list2 .__sizeof__(), "bytes")

    time_start_eval2 = time.time()
    half_list1 = (x for x in full_list1 if x < 5000)
    time_end_eval2 = time.time()
    print("Lazy evaluation filtering took:", time_end_eval2 - time_start_eval2, "seconds")
    print("half_list1 size in memory:", half_list1.__sizeof__(), "bytes")
    print(type(half_list1))

    time_start_non_eval2 = time.time()
    half_list2 = [x for x in full_list2 if x < 5000]
    time_end_non_eval2 = time.time()
    print("Non-lazy evaluation filtering took:", time_end_non_eval2 - time_start_non_eval2, "seconds")
    print("half_list2 size in memory:", half_list2.__sizeof__(), "bytes")
    print(type(half_list2))

if __name__ == "__main__":
    main()
