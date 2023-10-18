def main():
    base = int(input('Enter Base: '))
    pow = int(input('Enter Power: '))
    result = power(base, pow)
    print('{0} to Power of {1}= {2}'.format(base, pow, result))


def power(x, y):
    res = 1
    for value in range(1, y+1):
        res = res * x
    return res


main()
