def main():
    count = 1
    total = 0
    while count <= 5:
        value = int(input("Enter value {0}:".format(count)))
        total = total + value
        count = count + 1
    print("Sum of 5 values ={0}".format(total))


main()
