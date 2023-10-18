def main():
   list1 = [2, 6, 2, 7, 8, 4, 2, 6]
   result = allEven(list1)
   print('All Element Even List 1=  {0} '.format(result))

   list2 = [2, 6, 2, 8, 8, 4, 2, 6]
   result = allEven(list2)
   print('All Element Even List 2=  {0} '.format(result))


def allEven(listp):
   if len(listp)==0:
      return True
   else:
      el = listp.pop(0)
      if el % 2 == 0:
         return allEven(listp)
      else:
         return False

main()
