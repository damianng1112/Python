def main():
    val1 = int(input('Enter Value: '))
    result = factorial(val1)
    print('Factorial {0}= {1}'.format(val1, result))


def factorial(x):
    res = 1
    for value in range(1, x+1):
        res = res * value
    return res


main()
