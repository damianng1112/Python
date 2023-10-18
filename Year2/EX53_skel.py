

def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    target = int(input('Enter Target: '))
    result = countTarget(list1, target)
    print('{0} Occurs in List {1} Times'.format(target, result))

def countTarget(listp, tar):
    result = 0
    for el in listp:
        if el == tar:
            result = result + 1
    return result

main()
