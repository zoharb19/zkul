import random
import sys


def main():
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    rock_paper_scissors = [rock, paper, scissors]

    print("rock paper scissors!")
    print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
    user_input = input()
    pc_input = random.choice(rock_paper_scissors)

    while user_input != "q":
        if user_input == pc_input:
            print(f"{user_input} vs {pc_input}")
            print("its a tie")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_input = input()
            pc_input = random.choice(rock_paper_scissors)
        elif user_input == rock and pc_input == paper:
            print(f"{user_input} vs {pc_input}")
            print("pc won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_input = input()
            pc_input = random.choice(rock_paper_scissors)
        elif user_input == rock and pc_input == scissors:
            print(f"{user_input} vs {pc_input}")
            print("you won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_input = input()
            pc_input = random.choice(rock_paper_scissors)
        elif user_input == paper and pc_input == rock:
            print(f"{user_input} vs {pc_input}")
            print("you won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_input = input()
            pc_input = random.choice(rock_paper_scissors)
        elif user_input == paper and pc_input == scissors:
            print(f"{user_input} vs {pc_input}")
            print("pc won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_input = input()
            pc_input = random.choice(rock_paper_scissors)
        elif user_input == scissors and pc_input == paper:
            print(f"{user_input} vs {pc_input}")
            print("you won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_input = input()
            pc_input = random.choice(rock_paper_scissors)
        elif user_input == scissors and pc_input == rock:
            print(f"{user_input} vs {pc_input}")
            print("pc won")
            print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
            user_input = input()
            pc_input = random.choice(rock_paper_scissors)


if __name__ == '__main__':
    main()


