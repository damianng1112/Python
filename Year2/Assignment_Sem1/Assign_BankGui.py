from tkinter import *
from tkinter import messagebox
from Assign_Account import Account

window = Tk()
window.geometry("300x600")
window.title("Welcome")

# ============================================================
# Event Handling Methods


def display(index):
    global current
    global details
    details = detailsList[index]
    current = index
    entry2.delete(0, END)
    entry2.insert(END, details.getName())
    entry3.delete(0, END)
    entry3.insert(END, details.getAccountNo())
    entry4.delete(0, END)
    entry4.insert(END, "€")
    entry4.insert(END, details.getBalance())
    entry5.delete(0, END)
    entry5.insert(END, details.getAmount())
    entry6.delete(0, END)
    entry6.insert(END, details.getIntRate())
    entry6.insert(END, '%')
    entry7.delete(0, END)
    entry7.insert(END, '€')
    entry7.insert(END, details.calcTax(details.getIntRate()))
    bankrupt = details.getBankrupt()
    if bankrupt == True:
        var_cb1.set(1)
    else:
        var_cb1.set(0)
    memVar.set(details.getStatus())


def deposit():
    amount = float(entry5.get())
    details.deposit(amount)
    display(current)


def withdraw():
    amount = float(entry5.get())
    if amount > details.getBalance():
        warning()
    else:
        details.withdraw(amount)
    display(current)


def nextCmd():
    global current
    if current < (len(detailsList) - 1):
        current += 1
        display(current)


def prevCmd():
    global current
    if current > 0:
        current -= 1
        display(current)


def firstCmd():
    display(0)


def lastCmd():
    display(len(detailsList) - 1)


def insertNewDetails():
    name = entry2.get()
    accountNo = entry3.get()
    balance = entry4.get()
    bankrupt = False
    status = memVar.get()
    if var_cb1.get() == 1:
        bankrupt = True
    newDetails = Account(name, accountNo, balance, bankrupt, status)
    detailsList.append(newDetails)


def info():
    messagebox.showinfo('Info', 'Bank of TUS')


def refresh():
    display(current)


def warning():
    messagebox.showinfo("Warning", 'Cannot withdraw more than what you own!')


def myexit():
    exit()


def contacts():
    messagebox.showinfo('Contacts', 'Phone Number: 0123456789')

# End of Method Declarations
# ========================================================================


# Definitions
# =====================================================================

detail1 = Account("Damian", "37654457", 5000, False, 'Non-member')
detail2 = Account("Faithful", "35758475", 8000, False, 'Elite Member')
detail3 = Account("Natalia", "37857467", 10000, False, 'Member')
detail4 = Account("Ivan", "53354687", 4000, False, 'Member')
detail5 = Account("Ammar", "35675467", 7000, False, 'Elite Member')

detailsList = [detail1, detail2, detail3, detail4, detail5]

global current     # current details
global details
details = detailsList[0]  # initialize to first detail

# ========= End of Definitions ============================

# =======================================================
# Menu to Add New Detail
menu1 = Menu(window)  # MenuBar
window.config(menu=menu1)

subm1 = Menu(menu1)
menu1.add_cascade(label="Options", menu=subm1)
subm1.add_command(label="Insert Detail", command=insertNewDetails)
subm1.add_command(label='Exit', command=exit)
subm1.add_command(label='Refresh', command=refresh)
subm1.add_command(label='Info', command=info)

subm2 = Menu(menu1)
menu1.add_cascade(label='Help', menu=subm2)
subm2.add_command(label='Contacts', command=contacts)

# ======= End of Menu Definition ============================

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

label1 = Label(window, text="Banking Details", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=70, y=30)

label2 = Label(frame, text="Name", fg="blue", width=15, font=("arial", 10, "bold"))
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=1, sticky=W+E)

label3 = Label(frame, text="Account Number", fg="blue", width=15, font=("arial", 10, "bold"))
label3.grid(row=1, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=1, column=1, sticky=W+E)

label4 = Label(frame, text="Balance", fg="blue", width=15, font=("arial", 10, "bold"))
label4.grid(row=2, column=0, sticky=W+E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=1, sticky=W+E)

label5 = Label(frame, text="Amount", fg="blue", width=15, font=("arial", 10, "bold"))
label5.grid(row=3, column=0, sticky=W+E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=3, column=1, sticky=W+E)

var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Bankrupt", variable=var_cb1)
cb1.grid(row=4, column=0, columnspan=2)

label6 = Label(frame, text="Member status", fg="blue", width=15, font=("arial", 10, "bold"))
label6.grid(row=5, column=0, sticky=W+E)

list1 = ['Non-member', 'Member', 'Elite Member']
memVar = StringVar()
combo1 = OptionMenu(frame, memVar, *list1)
combo1.grid(row=5, column=1, sticky=W+E)

label7 = Label(frame, text="Interest Rate", fg="blue", width=15, font=("arial", 10, "bold"))
label7.grid(row=6, column=0, sticky=W+E)

entry6 = Entry(frame)
entry6.insert(END, '0')
entry6.grid(row=6, column=1, sticky=W+E)

label8 = Label(frame, text="Tax Amount", fg="blue", width=15, font=("arial", 10, "bold"))
label8.grid(row=7, column=0, sticky=W+E)

entry7 = Entry(frame)
entry7.insert(END, '0')
entry7.grid(row=7, column=1, sticky=W+E)

button1 = Button(frame, text="Deposit", fg="black", font=("arial", 10, "bold"), command=deposit)
button1.grid(row=8, column=0, sticky=W+E)

button2 = Button(frame, text="Withdraw", fg="black", font=("arial", 10, "bold"), command=withdraw)
button2.grid(row=8, column=1, sticky=W+E)

button3 = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
button3.grid(row=9, column=0, sticky=W+E)

button4 = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
button4.grid(row=9, column=1, sticky=W+E)

button5 = Button(frame, text="First", fg="black", font=("arial", 10, "bold"), command=firstCmd)
button5.grid(row=10, column=0, sticky=W+E)

button6 = Button(frame, text="Last", fg="black", font=("arial", 10, "bold"), command=lastCmd)
button6.grid(row=10, column=1, sticky=W+E)

canvas = Canvas(window, width=350, height=350)
canvas.place(x=30, y=400)
img = PhotoImage(file="bank.png")
canvas.create_image(120, 80, anchor=CENTER, image=img)

display(0)

mainloop()
