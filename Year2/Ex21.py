def main():
    val1 = int(input("Enter Value :"))
    val2 = int(input("Enter Value :"))
    add = val1 + val2
    mult = val1 * val2
    sub = val1 - val2
    print("Enter Option 1 to Add")
    print("Enter Option 2 to Mult")
    print("Enter Option 3 to Subtract")
    option = int(input("Enter Option Choice =>"))

    if option == 1:
        print("Add of {0}, {1} is {2}".format(val1, val2, add))
    elif option == 2:
        print("Mult of {0}, {1} is {2}".format(val1, val2, mult))
    elif option == 3:
        print("Subtract of {0}, {1} is {2}".format(val1, val2, sub))
    else:
        print("Did not enter a valid option")


main()
