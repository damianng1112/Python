


def addDigits(number):
   if number<10:
      return number
   else:
      last = number%10
      rest = int(number/10)
      return last + addDigits(rest)


def main():

   x = int(input('Enter number:'))
   result= addDigits(x)
   print('\nResult={0}'.format(result))

main()
