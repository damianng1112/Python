def main():
    print("  Ascii Table")
    print("-----------------")
    print("Letter  Ascii")
    value = 65
    while value < 75:
        letter = chr(value)
        print("  {0}      {1}".format(letter, value))
        value = value + 1


main()
