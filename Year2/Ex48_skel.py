
from tkinter import messagebox
from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def step():
    value = int(entry2.get())
    choice = var_radio.get()
    if choice == 1:
        value = value + 1
    elif choice == 2:
        value = value - 1
    entry2.delete(0, END)
    entry2.insert(END, value)


def reset():
    entry2.delete(0, END)
    entry2.insert(END, 0)


def info():
    messagebox.showinfo('Info', 'Hertz Car Rental')


def myexit():
    exit()


def contacts():
    messagebox.showinfo('Contacts', 'Phone Number: 0123456789')


menu1 = Menu(window)
window.config(menu=menu1)

subm1 = Menu(menu1)
menu1.add_cascade(label='Options', menu=subm1)
subm1.add_command(label='Reset', command=reset)
subm1.add_command(label='Exit', command=exit)
subm1.add_command(label='Info', command=info)

subm2 = Menu(menu1)
menu1.add_cascade(label='Help', menu=subm2)
subm2.add_command(label='Contacts', command=contacts)

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Radio Buttons", fg="blue", bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(frame, text="Value", fg="blue", width=15, font=("arial", 12, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '1')
entry2.grid(row=0, column=1, sticky=W+E)

var_radio = IntVar()  #1=incr,2=decr
r1 = Radiobutton(frame, text='Increment', variable=var_radio, value=1)
r1.grid(row=1, column=0, sticky=W+E)
r2 = Radiobutton(frame, text='Decrement', variable=var_radio, value=2)
r2.grid(row=1, column=1, sticky=W+E)

stepButton = Button(frame, text="Step", fg="black", font=("arial", 12, "bold"), command=step)
stepButton.grid(row=2, column=0, sticky=W+E)


mainloop()
