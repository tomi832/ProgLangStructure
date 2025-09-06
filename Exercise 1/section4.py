def is_prime_number(num, denom=2):
    """Check if a number is prime."""
    if num <= 2:
        return True
    if num % denom == 0:
        return False
    if num/denom <= 2:
        return True
    return is_prime_number(num, denom + 1)
print(is_prime_number(29))  # True
print(is_prime_number(15))  # False
print(is_prime_number(1))  # True
print(is_prime_number(2))  # True
print(is_prime_number(3))  # True
print(is_prime_number(4))  # False