

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

class Account:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def getName(self):
        return self.__name

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if self.__balance < amt:
            self.__balance
        else:
            self.__balance -= amt

#------------end of class definition------------------

def display():
    value1 = a1.getName()
    value2 = a1.getBalance()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)




def depositEvent():
    amt=int(entry4.get())
    a1.deposit(amt)
    display()


def withdrawEvent():
    amt = int(entry5.get())
    a1.withdraw(amt)
    display()


a1=Account("J.Smith",500)


label1 = Label(window, text="Account Details", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Name", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Balance", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)



button4= Button(window, text="Deposit", fg="black", font=("arial", 10, "bold"), command=depositEvent)
button4.place(x=40, y=140)

entry4 = Entry(window)
entry4.insert(END, '30')
entry4.place(x=120, y=140)

button5= Button(window, text="Withdraw", fg="black", font=("arial", 10, "bold"), command=withdrawEvent)
button5.place(x=40, y=180)

entry5 = Entry(window)
entry5.insert(END, '20')
entry5.place(x=120, y=180)


display()

mainloop()
