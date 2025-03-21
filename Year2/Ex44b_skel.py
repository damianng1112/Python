
from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def stepup():

    value1 = float(entry2.get())
    value2 = float(stepUpVar.get())
    value1 = value1 * value2
    entry2.delete(0, END)
    entry2.insert(END, value1)


def stepdown():

    value1 = float(entry2.get())
    value2 = float(stepDownVar.get())
    value1 = value1 / value2
    entry2.delete(0, END)
    entry2.insert(END, value1)


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Grid example", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen


label2 = Label(frame, text="Value", fg="blue", width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '1')
entry2.grid(row=0, column=1, sticky=W+E)

button1 = Button(frame, text="Multiply", fg="black", font=("arial", 10, "bold"), command=stepup)
button1.grid(row=1, column=0, sticky=W+E)

button2 = Button(frame, text="Divide", fg="black", font=("arial", 10, "bold"), command=stepdown)
button2.grid(row=2, column=0, sticky=W+E)

# entry3 = Entry(frame)
# entry3.insert(END, '1')
# entry3.grid(row=1,column=1, sticky=W+E)
list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
stepUpVar = StringVar()
combo1 = OptionMenu(frame, stepUpVar, *list1)
stepUpVar.set("1")
combo1.grid(row=1, column=1, sticky=W+E)

stepDownVar = StringVar()
combo2 = OptionMenu(frame, stepDownVar, *list1)
stepDownVar.set('1')
combo2.grid(row=2, column=1, sticky=W+E)

mainloop()
