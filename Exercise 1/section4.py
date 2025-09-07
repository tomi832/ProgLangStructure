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
    userInput = input("Enter prime number:")
    try:
        number = int(userInput)
        return number
    except ValueError:
        print("invalid input")
        return input_number()


def main():
    userInput = input("Enter prime number:")
    try:
        number = int(userInput)
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