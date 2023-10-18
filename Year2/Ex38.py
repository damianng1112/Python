def main():
    length = int(input('Enter Length: '))
    display(length)


def display(x):
    for value in range(1, x+1):
        print(' *', end='')


main()
