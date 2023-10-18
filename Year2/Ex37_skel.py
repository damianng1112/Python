def main():
    height = int(input('Enter Height: '))
    display(height)


def display(x):
    for value in range(1, x+1):
        print(' *')


main()
