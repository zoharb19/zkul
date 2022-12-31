
def primes(a_number):
    # prime number only divides by itself and 1
    for i in range(2, a_number):
        if a_number % i == 0:
            return "not a prime"
        else:
            i = i + 1
            if a_number == i:
                return "a prime"


def main():
    print("choose a num")
    num = int(input())
    print(primes(num))


if __name__ == '__main__':
    main()

