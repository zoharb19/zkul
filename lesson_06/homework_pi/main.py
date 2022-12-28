# pi = + 4/1 - 4/3 + 4/5 - 4/7...
def pi_calculate(number_of_calculations):

    pi = 0
    bottom_part = 1
    for i in range(number_of_calculations):
        if i % 2 == 0:
            pi += 4/bottom_part
            bottom_part += 2
        else:
            pi -= 4/bottom_part
            bottom_part += 2
    return pi


def main():

    print(pi_calculate(100000000))


if __name__ == '__main__':
    main()


