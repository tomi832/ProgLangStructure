def sum_digit(n: str):
    """Returns the sum of the digits of n."""
    negative = False
    if n[0] == '-':
        negative = True
        if not str(n[1:]).isdecimal():
            return "invalid input"
    elif not str(n).isdecimal():
        return "invalid input"
    return -sum(map(int, n[1:])) if negative else sum(map(int, n))
    # this went through multiple iterations, previously I accidentally violated FP
    # by doing stuff like n = n[1:] or having 2 variables

def main():
    print("enter number:")
    userInput = input()
    print(sum_digit(userInput))

if __name__ == "__main__":
    main()