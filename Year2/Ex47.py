

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def getprice():
    carSize = carSizeVar.get()
    passengers = int(passengersVar.get())
    days = int(daysVar.get())
    if passengers > 5:
        price = 120 * days
    elif carSize == "Small":
        price = days * 50
    elif carSize == 'Medium':
        price = days * 70
    elif carSize == 'Large':
        price = days * 90
    if var_cb1.get() > 0:
        price = price + (10 * days)
    if var_cb2.get() > 0:
        price = price + (5 * days)
    entry3.delete(0, END)
    entry3.insert(END, "€")
    entry3.insert(END, price)


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Car Loan Application", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=40, y=30)                            # place on screen


label2 = Label(frame, text="Car Type", fg="blue", width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

label3 = Label(frame, text="Days", fg="blue", width=15, font=("arial", 10, "bold"))   #
label3.grid(row=1, column=0, sticky=W+E)

label4 = Label(frame, text="Passengers", fg="blue", width=15, font=("arial", 10, "bold"))   #
label4.grid(row=3, column=0, sticky=W+E)

list1 = ['Small', 'Medium', 'Large']
carSizeVar = StringVar()
combo1 = OptionMenu(frame, carSizeVar, *list1)
carSizeVar.set("Medium")
combo1.grid(row=0, column=1, sticky=W+E)

list2 = ['1', '2', '3', '4', '5', '6', '7']
daysVar = StringVar()
combo2 = OptionMenu(frame, daysVar, *list2)
daysVar.set("1")
combo2.grid(row=1, column=1, sticky=W+E)

list3 = ['1', '2', '3', '4', '5', '6', '7']
passengersVar = StringVar()
combo3 = OptionMenu(frame, passengersVar, *list2)
passengersVar.set("1")
combo3.grid(row=3, column=1, sticky=W+E)

var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Insurance", variable=var_cb1)
cb1.grid(row=2, column=0, columnspan=2)

var_cb2 = IntVar()  # 0 unchecked, 1 checked
cb2 = Checkbutton(frame, text="Sat Nav", variable=var_cb2)
cb2.grid(row=4, column=0, columnspan=2)

button1 = Button(frame, text="GetPrice", fg="black", font=("arial", 10, "bold"), command=getprice)
button1.grid(row=5, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, "0")
entry3.grid(row=5, column=1, sticky=W+E)

mainloop()
