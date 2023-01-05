
def main():
    rows = 6
    columns = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            print(j - 1, end="")
        print()
        columns = columns + 1


if __name__ == '__main__':
    main()

