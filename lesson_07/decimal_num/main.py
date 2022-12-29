
def primes(prime):
    for i in range(2, prime):
        # check if prime % == 0 if so its not prime
        if prime % i == 0:
            print(f"{prime} is not a prime")
            break

        else:
            print(f"{prime} is a prime")
            break


def main():
    print(f"choose a num")
    num = int(input())
    primes(num)


if __name__ == '__main__':
    main()

