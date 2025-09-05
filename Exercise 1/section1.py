def get_penta_nums(n):
    """Return the nth pentagonal number."""
    return n * (3 * n - 1) // 2

def penta_num_range(n1, n2):
    """Generate a list of pentagonal numbers in the range from n1 to n2 (exclusive)."""
    return list(map(get_penta_nums, range(n1, n2)))