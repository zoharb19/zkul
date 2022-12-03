import random


def main():
    random_num = random.randint(1, 10)
    guess = 0
    while random_num != guess:
        guess = int(input("take a guess: "))
        if random_num > guess:
            print("too low try again")
        elif random_num < guess:
            print("too high")
    else:
        print("you won")


if __name__ == '__main__':
    main()
