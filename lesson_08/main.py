#nested loops!


def main():
    current = table_of_multiplication
    current()


def table_of_multiplication():
    rows = 10
    columns = 10
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            print(f'{i * j:02d}', end=" ")
        print()


if __name__ == '__main__':
    main()

