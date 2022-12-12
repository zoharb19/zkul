import random
import sys


def main():
    r = "rock"
    p = "paper"
    s = "scissors"
    rps = [r, p, s]

    print("rock paper scissors!")
    print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
    user_inp = input()
    pc_inp = random.choice(rps)

    while user_inp != "q":
        if user_inp == pc_inp:
            print(f"{user_inp} vs {pc_inp}")
            print("its a tie")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_inp = input()
            pc_inp = random.choice(rps)
        elif user_inp == r and pc_inp == p:
            print(f"{user_inp} vs {pc_inp}")
            print("pc won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_inp = input()
            pc_inp = random.choice(rps)
        elif user_inp == r and pc_inp == s:
            print(f"{user_inp} vs {pc_inp}")
            print("you won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_inp = input()
            pc_inp = random.choice(rps)
        elif user_inp == p and pc_inp == r:
            print(f"{user_inp} vs {pc_inp}")
            print("you won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_inp = input()
            pc_inp = random.choice(rps)
        elif user_inp == p and pc_inp == s:
            print(f"{user_inp} vs {pc_inp}")
            print("pc won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_inp = input()
            pc_inp = random.choice(rps)
        elif user_inp == s and pc_inp == p:
            print(f"{user_inp} vs {pc_inp}")
            print("you won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_inp = input()
            pc_inp = random.choice(rps)
        elif user_inp == s and pc_inp == r:
            print(f"{user_inp} vs {pc_inp}")
            print("pc won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_inp = input()
            pc_inp = random.choice(rps)
        else:
            sys.exit()


if __name__ == '__main__':
    main()


