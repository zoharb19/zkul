
def primes(a_number):
    # prime number only divides by itself and 1
    for i in range(2, a_number):
        if a_number % i == 0:
            return False
        else:
            i = i + 1
            if a_number == i:
                return True


def main():
    num = int(input())
    if primes(num) is False:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")


if __name__ == '__main__':
    main()

