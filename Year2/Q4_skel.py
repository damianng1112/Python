

def main():
    value = 99
    count = 0
    while value > 0:
        value=int(input('Enter Value 1-99 (negative number to stop):'))
        if value <10 and value > 0:
            count+=1
    print('Number of Single Digit Elements Entered= {0}'.format(count))


main()
