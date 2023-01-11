def triforce(columns, rows):
    for i in range(1, rows):
        for j in range(1, columns + 1):
            print(j, end=" ")
        print()
        columns = columns + 1
    for k in range(1, rows + 1):
        for l in range(1, columns - 1):
            print(l, end=" ")
        print()
        columns -= 1


def main():
    triforce(1, 6)


if __name__ == '__main__':
    main()

