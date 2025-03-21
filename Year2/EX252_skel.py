
class Money:
    def __init__(self, e, c):
        self.euro = e 
        self.cent = c

    def printMoney(self):
        print('€{0}.{1}'.format(self.euro,self.cent))
        
    # Add   __iadd__(self, other): and    __sub__(self, other):
    def __iadd__(self, other):
        result = Money(self.euro + other.euro, self.cent + other.cent)
        if result.cent > 99:
            result.euro += 1
            result.cent -= 100
        return result

    def __sub__(self, other):
        while self.euro > 0:
            self.euro -= 1
            self.cent += 100
        while other.euro > 0:
            other.euro -= 1
            other.cent += 100
        total = self.cent - other.cent
        euro = int(total/100)
        remainCent = total % 100
        result = Money(euro, remainCent)
        return result

def main():
    m1 = Money(2,43)
    m2 = Money(5,29)
    m3 = Money(9,73)
    res1 = m2 - m1
    print('\n(5.29 - 2.43= ',end='')
    res1.printMoney()

    res2 = m3 - m2
    print('\n (9.73 - 5.29= ',end='')
    res2.printMoney()
    
    m3+= m1
    print('\n (9.73 += 2.43= ',end='')
    m3.printMoney()
main()
