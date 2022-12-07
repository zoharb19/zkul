import random


def main():
    random_num = random.randint(0, 10)
    print("this is guess the number game")
    guess = int(input())
    for guess_taken in (0, 5):
        print("guess a number: " + str(guess))
        if guess < random_num:
            print("number too low")
        elif guess > random_num:
            print("guess is too high")
        else:
            break
    

if __name__ == '__main__':
    main()
