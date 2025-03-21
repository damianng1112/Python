

from tkinter import *
window = Tk()
window.geometry("300x360")
window.title("Welcome")

from Ex225MyClasses import *


#------------end of class definition------------------

def display():
    value1 = t1.getName()
    value2 = t1.getTitle()
    value3 = t1.getLicence()
    value4 = t1.getPosition()
    value5 = t1.getGamesPlayed()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, value4)
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, value5)

def changeTitleEvent():
    newTitle = entry3a.get()
    t1.setTitle(newTitle)
    display()

def resetLicenceEvent():
    newLicence = entry3b.get()
    t1.setLicence(newLicence)
    display()

def resetGamesPlayedEvent():
    t1.incrementGamesPlayed()
    display()

def closeEvent():
    window.destroy()

t1=PlayerCoach("J.Smith","Assistant Mgr", "Uefa B","Striker", 134)


label1 = Label(window, text="PlayerCoach Details", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=40, y=30)                            # place on screen

label2 = Label(window, text="Name", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=130, y=80)

label3 = Label(window, text="Title", fg="blue", width=12, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=130, y=110)

label4 = Label(window, text="Licence", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=130, y=140)

label5 = Label(window, text="Position", fg="blue", width=12, font=("arial", 10, "bold"))   #
label5.place(x=10, y=170)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=130, y=170)

label6 = Label(window, text="GamesPlayed", fg="blue", width=11, font=("arial", 10, "bold"))   #
label6.place(x=10, y=200)

entry6 = Entry(window)
entry6.insert(END, '')
entry6.place(x=130, y=200)

#-------------------------------
button1= Button(window, text="changeTitle", fg="black", font=("arial", 10, "bold"), command=changeTitleEvent)
button1.place(x=2, y=230)

entry3a = Entry(window)
entry3a.insert(END, 'Manager')
entry3a.place(x=130, y=230)

#button2= Button(window, text="Exit", fg="black", font=("arial", 10, "bold"), command=exitEvent)
#button2.place(x=120, y=230)

button3= Button(window, text="updateLicence", fg="black", font=("arial", 10, "bold"), command=resetLicenceEvent)
button3.place(x=2, y=260)

entry3b = Entry(window)
entry3b.insert(END, 'Uefa A')
entry3b.place(x=130, y=260)

button4= Button(window, text="GamesPlayed++", fg="black", font=("arial", 10, "bold"), command=resetGamesPlayedEvent)
button4.place(x=2, y=290)

button5= Button(window, text="Exit", fg="black", font=("arial", 10, "bold"), command=closeEvent)
button5.place(x=130, y=290)



display()

mainloop()
