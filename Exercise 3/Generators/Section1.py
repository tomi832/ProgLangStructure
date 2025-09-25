import time

def lazy_eval():
    for i in range(10000):
        yield i

def non_lazy_eval():
    return [x for x in range(10000)]


def main():
    # it is not super clear to me what the assignment wants. it asks for a list of 10000 elements, but also to use lazy evaluation.
    # Now, a generator is not a list, but making it into a list will not help us at all. it will take just as much time and memory to
    # create the list as it would to create the list in the non-lazy evaluation (this is what i did at first so i know).
    # So I assume the assignment wants us to compare the time it takes to create the generator vs the time it takes to create the list.
    time_start_eval = time.time()
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
