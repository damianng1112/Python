def main():
    list1= [2, 5, 8, 2, 8, 7, 2]
    target = int(input('Enter Target: '))
    result = countTarget(list1, target)
    print('Element {0} found in list = {1} Times'.format(target, result))

def countTarget(listp, tar):
    res = 0
    for el in listp:
        if el == tar:
            res +=1
    return res

main()

