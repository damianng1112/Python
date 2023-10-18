
class Money:
    def __init__(self, e, c):
        self.euro = e 
        self.cent = c

    def printMoney(self):
        print('€{0}.{1}'.format(self.euro, self.cent))
        
     # complete add, gt
    def __add__(self, other):
        result = Money(self.euro + other.euro, self.cent + other.cent)
        if result.cent > 99:
            result.euro += 1
            result.cent -= 100
        return result

    def __gt__(self, other):
        if self.euro == other.euro:
            if self.cent > other.cent:
                return True
            else:
                return False
        elif self.euro > other.euro:
            return True
        else:
            return False


def main():
    m1 = Money(2,43)
    m2 = Money(3,29)
    m3 = Money(4,73)
    res1 = m1 + m2
    print('\n(2.43 + 3.29= ',end='')
    res1.printMoney()

    res2 = m1 + m3
    print('\n (2.43 + 4.73= ',end='')
    res2.printMoney()
    
    if (m1 > m2):
        print('\n2.43 > 3.29')
    if (m3 > m1):
        print('\n4.73 > 3.29')
main()
