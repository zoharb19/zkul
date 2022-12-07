import random
import sys


def main():
    max_num = 10
    # 1. generate random number
    random_num = random.randint(0, max_num)
    # 2. loop for 5 times:
    for try_num in range(10):
        # 2.1 ask player to choose a number in range
        print(f"choose a number between 0 to {max_num}")
        # 2.2 player insert input
        player_num = int(input())
        # 2.3 if right:
        if player_num == random_num:
            # 2.3.1 print you won
            print("YOU WON")
            # 2.3.2 exit game
            sys.exit(0)
        # 2.4 else:
        else:
            # 2.4.1 print if higher or lower
            if player_num > random_num:
                print("your number is too high")
            else:
                print("your number is too low")


if __name__ == '__main__':
    main()
