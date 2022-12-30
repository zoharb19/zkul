
def primes(a_number):
    for i in range(2, a_number - 1):
        if a_number % i == 1:

            print(f"{a_number} is a prime")
            break
        else:
            print(f"{a_number} is not prime")
            break


def main():
    print("choose a num")
    num = int(input())
    primes(num)


if __name__ == '__main__':
    main()

