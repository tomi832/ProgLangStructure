def sum_array(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])


def sum_array_tail(arr, accumulative=0):
    if len(arr) == 0:
        return accumulative
    else:
        return sum_array_tail(arr[1:], accumulative + arr[0])