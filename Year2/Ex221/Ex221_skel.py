

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

from Ex221MyClasses import *

#------------end of class definition------------------

def display():
    value1 = p1.getValue1()
    value2 = p1.getValue2()
    value3 = p1.getValue3()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, value3)


def incrV1Event():
    p1.incrValue1()
    display()

def incrV2Event():
    p1.incrValue2()
    display()

def incrV3Event():
    p1.incrValue3()
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


p1=Treble(3,5,2)


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

label4 = Label(window, text="Value3", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=140)

entry6 = Entry(window)
entry6.insert(END, '1')
entry6.place(x=120, y=140)

button1 = Button(window, text="IncrementV1", fg="black", font=("arial", 10, "bold"), command=incrV1Event)
button1.place(x=0, y=170)

button2 = Button(window, text="IncrementV2", fg="black", font=("arial", 10, "bold"), command=incrV2Event)
button2.place(x=95, y=170)

button3 = Button(window, text="IncrementV3", fg="black", font=("arial", 10, "bold"), command=incrV3Event)
button3.place(x=195, y=170)

button4= Button(window, text="Add", fg="black", font=("arial", 10, "bold"), command=addEvent)
button4.place(x=40, y=200)

entry4 = Entry(window)
entry4.insert(END, '')
entry4.place(x=120, y=200)

button5= Button(window, text="Multiply", fg="black", font=("arial", 10, "bold"), command=multiplyEvent)
button5.place(x=40, y=230)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=120, y=230)


display()

mainloop()
