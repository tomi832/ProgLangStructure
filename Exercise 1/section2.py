def sum_digit(n: str):
    """Returns the sum of the digits of n."""
    if not str(n).isdecimal():
        return "invalid input"
    return sum(map(int, str(n)))

def main():
    userInput = input("Please enter a number:")
    print(sum_digit(userInput))

if __name__ == "__main__":
    main()