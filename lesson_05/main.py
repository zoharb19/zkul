import random
import sys


def main():
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    rock_paper_scissors = [rock, paper, scissors]

    print("rock paper scissors!")
    user_input = None

    while user_input != "q":
        print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
        user_input = input()
        pc_input = random.choice(rock_paper_scissors)
        print(f"{user_input} vs {pc_input}")

        if user_input == "q":
            break
        elif user_input == pc_input:
            print("its a tie")
        elif user_input == rock and pc_input == paper:
            print("pc won")
        elif user_input == rock and pc_input == scissors:
            print("you won")
        elif user_input == paper and pc_input == rock:
            print("you won")
        elif user_input == paper and pc_input == scissors:
            print("pc won")
        elif user_input == scissors and pc_input == paper:
            print("you won")
        elif user_input == scissors and pc_input == rock:
            print("pc won")
        else:
            print("only rock paper scissors and Q allowed !!!")


if __name__ == '__main__':
    main()


