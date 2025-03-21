

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

class Pair:

    def __init__(self, val1, val2):
        self.__value1=val1
        self.__value2=val2

    def getValue1(self):
        return self.__value1

    def setValue1(self,val1):
        self.__value1=val1

    def getValue2(self):
        return self.__value2

    def setValue2(self, val2):
        self.__value1 = val2

    def incrValue1(self):
        self.__value1+=1

    def incrValue2(self):
        self.__value2+=1

    def add(self):
        res = self.__value1 + self.__value2
        return res

    def multiply(self):
        res = self.__value1 * self.__value2
        return res

#------------end of class definition------------------

def display():
    value1 = p1.getValue1()
    value2 = p1.getValue2()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)

def incrV1Event():
    p1.incrValue1()
    display()

def incrV2Event():
    p1.incrValue2()
    display()


def addEvent():
    result= p1.add()
    display()
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, result)

def multiplyEvent():
    result = p1.multiply()
    display()
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, result)


p1=Pair(3,5)


label1 = Label(window, text="Welcome", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Value1", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Value2", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)


button1 = Button(window, text="IncrementV1", fg="black", font=("arial", 12, "bold"), command=incrV1Event)
button1.place(x=10, y=140)

button2 = Button(window, text="IncrementV2", fg="black", font=("arial", 12, "bold"), command=incrV2Event)
button2.place(x=140, y=140)

button4= Button(window, text="Add", fg="black", font=("arial", 10, "bold"), command=addEvent)
button4.place(x=40, y=180)

entry4 = Entry(window)
entry4.insert(END, '')
entry4.place(x=120, y=180)

button5= Button(window, text="Multiply", fg="black", font=("arial", 10, "bold"), command=multiplyEvent)
button5.place(x=40, y=220)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=120, y=220)


display()

mainloop()
