import random


def report_winner(winner):
    if winner is None:
        print(f"its a tie")
    else:
        print(f"{winner} won")


def main():
    quit_game = "q"
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    rock_paper_scissors = [rock, paper, scissors]

    print("rock paper scissors!")
    user_input = None

    while user_input != quit_game:
        print("choose your weapon: Rock, Paper, Scissors or Q to quit:")
        user_input = input()
        pc_input = random.choice(rock_paper_scissors)
        if user_input == quit_game:
            print("bye")
        elif user_input != pc_input or user_input == pc_input:
            print(f"{user_input} vs {pc_input}")

        if user_input == quit_game:
            break
        elif user_input == pc_input:
            report_winner(None)
        elif user_input == rock and pc_input == paper:
            report_winner("pc")
        elif user_input == rock and pc_input == scissors:
            report_winner("you")
        elif user_input == paper and pc_input == rock:
            report_winner("you")
        elif user_input == paper and pc_input == scissors:
            report_winner("pc")
        elif user_input == scissors and pc_input == paper:
            report_winner("you")
        elif user_input == scissors and pc_input == rock:
            report_winner("pc")
        else:
            print("only rock paper scissors and Q allowed !!!")


if __name__ == '__main__':
    main()


