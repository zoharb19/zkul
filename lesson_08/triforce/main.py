def triforce(columns, rows):
    for i in range(1, rows):
        for j in range(1, columns + 1):
            print(j, end="")
        print()
        columns = columns + 1
        if i == rows - 1:
            for i in range(1, rows + 1):
                for j in range(1, columns - 1):
                    print(j, end="")
                print()
                columns -= 1


def main():
    triforce(1, 105)


if __name__ == '__main__':
    main()

