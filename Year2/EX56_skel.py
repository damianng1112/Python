

def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    lower = int(input('Enter Lower Limit: '))
    upper = int(input('Enter Upper Limit: '))
    result = allInRange(list1, lower, upper)
    print('{0} = All of element between {1} and {2} inclusive'.format(result, lower, upper))


def allInRange(listp, low, high):
    for el in listp:
        if low > el or el > high:
            return False
        else:
            return True


main()
