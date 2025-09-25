def gcd(a, b):
    """
    Recursive Euclidean algorithm for GCD, which stands for Greatest Common Divisor.
    found this when I searched for a way to solve this problem
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm_rec(a, b):
    """Find the least common multiple of two numbers using recursion."""
    return abs(a * b) // gcd(a, b)

############

def lcm_rec_tail(a, b, multiple):
    """Helper function to find the least common multiple using recursion."""
    if multiple % a == 0 and multiple % b == 0:
        return multiple
    return lcm_rec_tail(a, b, multiple + 1)
