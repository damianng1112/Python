

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def add():
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    res = value1 + value2
    entry4.delete(0, END)
    entry4.insert(END, res)


def sub():
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    res = value1 - value2
    entry5.delete(0, END)
    entry5.insert(END, res)


label1 = Label(window, text="Calculator", fg="blue", bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=10)                            # place on screen

label2 = Label(window, text="Value1", fg="blue", width=10, font=("arial", 12, "bold"))   #
label2.place(x=10, y=50)

label3 = Label(window, text="Value2", fg="blue", width=10, font=("arial", 12, "bold"))   #
label3.place(x=10, y=90)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=50)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=90)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=130, y=160)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=130, y=200)

button1 = Button(window, text="Add", fg="black", width=7, font=("arial", 12, "bold"), command=add)
button1.place(x=40, y=160)

button2 = Button(window, text='Subtract', fg='black', width=7, font=('arial', 12, 'bold'), command=sub)
button2.place(x=40, y=200)

mainloop()
