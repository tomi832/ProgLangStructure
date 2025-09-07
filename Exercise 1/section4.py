def is_prime_number(num, denom=2):
    if num <= 0:
        return False
    if num <= 2:
        return True
    if num % denom == 0:
        return False
    if num/denom <= 2:
        return True
    return is_prime_number(num, denom + 1)


def get_twin_prime_for(num):
    if is_prime_number(num - 2):
        return num - 2
    if is_prime_number(num + 2):
        return num + 2
    return None


def input_number():
    user_input = input("Enter prime number:")
    try:
        number = int(user_input)
        return number
    except ValueError:
        print("invalid input")
        return input_number()

# result being initialized to None was suggested by PyCharm itself, and I looked it up in chatgpt why is it important.
# he said it's because using mutable default arguments can lead to unexpected behavior, because the same object will be
# initialized once when the function is defined, and then we use the same one in every call to the function.
def get_twin_primes_dict(n, current=2, result=None):
    if result is None:
        result = {}
    if current > n:
        return result
    if is_prime_number(current) and get_twin_prime_for(current) is not None:
        # had to use chatgpt to figure out the ** syntax
        return get_twin_primes_dict(n, current + 1, {**result, current: get_twin_prime_for(current)})
    return get_twin_primes_dict(n, current + 1, result)

def main():
    user_input = input("Enter prime number:")
    try:
        number = int(user_input)
    except ValueError:
        print("invalid input")
        return
    if is_prime_number(number):
        twin_number = get_twin_prime_for(number)
        if twin_number is not None:
            print(twin_number)
        else:
            print(f"invalid input")
    else:
       print(f"invalid input")


if __name__ == "__main__":
    main()