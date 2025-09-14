import time
from functools import reduce

list = [x for x in range(10001)]

"""
i wrote it as a function so you can import it. the logic still exists as is 
in the main function for the excersise sake, to measure time and compare.
i dont want to call this function in main for potential time loss while calling it.
"""
def sum_transformed_list(list):
    transformed_list = map(lambda x: x / 2 + 2, list)
    summed_list = reduce(lambda x, y: x + y, transformed_list)
    return summed_list


if __name__ == "_main_":
    # start time measurement
    time_start = time.time()
    # subsection 1
    transformed_list = map(lambda x: x / 2 + 2, list)
    # subsection 2
    summed_list = reduce(lambda x, y: x + y, transformed_list)
    time_end = time.time()
    print("time passed with map and reduce: ", time_end - time_start)

    time_start = time.time()
    transformed_list = []
    for i in range(len(list)):
        transformed_list.append(list[i] / 2 + 2)
    summed_list = 0
    for i in range(len(transformed_list)):
        summed_list += transformed_list[i]
    time_end = time.time()
    print("time passed with for loops: ", time_end - time_start)

    # subsection 4
    transformed_and_summed = reduce(
        lambda x, y: x + y / 2 + 2, map(lambda x: x / 2 + 2, list)
    )
