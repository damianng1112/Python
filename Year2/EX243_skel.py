def main():
    set1 = {2, 5, 2, 8, 7}
    set2 = {1, 2, 3, 4, 5, 6, 7}
    target1 = int(input('Enter Target 1: '))
    target2 = int(input('Enter Target 2: '))
    result = inBoth2(set1, set2, target1, target2)
    print('Element {0} & {1} found in both sets = {2}'.format(target1, target2, result))


def inBoth(setp1, setp2, tar1, tar2):
    setp3 = setp1.intersection(setp2)
    res1 = False
    res2 = False
    result = False
    for el in setp3:
        if el == tar1:
            res1 = True
        if el == tar2:
            res2 = True
    if res1 == True & res2 == True:
        result = True
    return result


def inBoth2(setp1, setp2, tar1, tar2):
    setp3 = setp1.intersection(setp2)
    setp4 = {tar2, tar1}
    return setp4.issubset(setp3)


main()
