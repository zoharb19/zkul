
def main():
    rows = 10
    columns = 1
    for i in range(1, rows):
        for j in range(1, columns + 1):
            print(j, end="")
        print()
        columns = columns + 1
        

if __name__ == '__main__':
    main()

