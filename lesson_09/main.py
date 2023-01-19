

def main():
    while True:
        user_input = input("enter a number:")

        try:
            converted_to_int = int(user_input)
            print(f"you entered: {converted_to_int}")
            break
        except ValueError:
            print("this is not a number")


if __name__ == '__main__':
    main()

