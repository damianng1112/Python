

def main():
    val1 =  int(input('Enter Value: '))
    val2 =  int(input('Enter Value: '))
    val3 = int(input('Enter Value: '))
    result = my_max(val1, val2, val3)
    print('Max= {0}'.format(result))

def my_max(x, y, z):
    res = 0
    if (x>y) & (x>z):
        res = x
    elif (y>x) & (y>z):
        res = y
    else:
        res = z
    return res

main()
