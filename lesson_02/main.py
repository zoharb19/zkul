def main():
    print('henlo im dog')
    print('who are you?')
    user_name = input()
    print('hello mr. ' + user_name)
    print('your name length is ' + str(len(user_name)))
    print('how old are you?')
    user_age = input()
    user_newage = int(user_age) + 2
    print('in 2 years you will be ' + str(user_newage) + ' years old')


if __name__ == "__main__":
    main()
  