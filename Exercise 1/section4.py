def is_prime_number(num, denom=2):
    """Check if a number is prime."""
    if num <= 2:
        return True
    if num % denom == 0:
        return False
    if num/denom <= 2:
        return True
    return is_prime_number(num, denom + 1)

"""new main function instead of being in the if statement"""
def main():
    number = int(input("Enter a number, or a negative number to exit: "))
    while number >= 0:
        if is_prime_number(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
        number = int(input("Enter a number, or a negative number to exit: "))


if __name__ == "__main__":
    main()