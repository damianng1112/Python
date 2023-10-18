def main():
    width = int(input('Enter Width: '))
    display(width)


def display(x):
    for value1 in range(1, x+1):
        for value2 in range(1, x+1):
            print(' * ', end='')
        print('')


main()
