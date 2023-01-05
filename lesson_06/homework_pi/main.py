# pi = + 4/1 - 4/3 + 4/5 - 4/7...
def pi_calculate(number_of_calculations):
    result = 0
    top = 4

    for i in range(number_of_calculations):
        bottom = i * 2 + 1
        mana = top/bottom
        if i % 2 == 0:
            result += mana
        else:
            result -= mana
    
    return result


def main():    
    print(pi_calculate(3000000000000))

    
if __name__ == '__main__':
    main()


