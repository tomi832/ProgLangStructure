import time
from functools import reduce

l = [x for x in range(10001)]

"""
i wrote it as a function so you can import it. the logic still exists as is 
in the main function for the excersise sake, to measure time and compare.
i dont want to call this function in main for potential time loss while calling it.
"""
def sum_transformed_list(list):
    transformed_list = map(lambda x: x / 2 + 2, list)
    sum = reduce(lambda x, y: x + y, transformed_list)
    return sum


if __name__ == "_main_":
    # start time measurement
    time_start = time.time()
    # subsection 1
    transformed_list = map(lambda x: x / 2 + 2, l)
    # subsection 2
    sum = reduce(lambda x, y: x + y, transformed_list)
    time_end = time.time()
    print("time passed with map and reduce: ", time_end - time_start)

    time_start = time.time()
    transformed_list = []
    for i in range(len(l)):
        transformed_list.append(l[i] / 2 + 2)
    sum = 0
    for i in range(len(transformed_list)):
        sum += transformed_list[i]
    time_end = time.time()
    print("time passed with for loops: ", time_end - time_start)

    # subsection 4
    transformed_and_summed = reduce(
        lambda x, y: x + y / 2 + 2, map(lambda x: x / 2 + 2, l)
    )
