def main():
    import random
    random_num = random.randint(0, 10)
    guess = int(input("choose a number between 0 and 10: "))
    while guess != random_num:
        if random_num > guess:
            print("too low try again                           ◝ʕ •ᴥ• ʔ◜")
            guess = int(input("choose a number between 0 and 10: "))

        if random_num < guess:
            print("too high try again                          ʕノ•ᴥ•ʔノ ︵ ┻━┻")
            guess = int(input("choose a number between 0 and 10: "))

    else:
        print("you won!                                     ʕ　·ᴥ·ʔ人ʕ·ᴥ·　ʔ ")


if __name__ == '__main__':
    main()
