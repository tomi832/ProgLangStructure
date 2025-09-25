from math import floor


def gen_primes():
    main_num = 2
    while True:
        is_prime = True
        for p in range(2, floor(main_num / 2) + 1):
            if main_num % p == 0:
                is_prime = False
                break
        if is_prime:
            yield main_num
        main_num += 1

# main function to test the generator
def main():
    prime_gen = gen_primes()
    for _ in range(20):
        print(next(prime_gen))

if __name__ == "__main__":
    main()