from tkinter import *

window = Tk()
window.title("Project_Resturant_BQ4_2025_08_21")
window.geometry("525x750")
window.resizable(False, False)

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()
num5 = IntVar()
num6 = IntVar()
num7 = IntVar()
bill_var = IntVar()
paid_var = IntVar()
balance_var = IntVar()

mainTitle = Label(window, text="KARACHI FOODS(BILL)", font=("Arial", 25))
mainTitle.place(x=70, y=45)

# Labels
Label(window, text="Pizza:", font=("Arial", 15)).place(x=61, y=125)
Label(window, text="Burgers:", font=("Arial", 15)).place(x=61, y=166)
Label(window, text="Broast:", font=("Arial", 15)).place(x=61, y=208)
Label(window, text="Fries:", font=("Arial", 15)).place(x=61, y=250)
Label(window, text="Drinks:", font=("Arial", 15)).place(x=61, y=292)
Label(window, text="Desserts:", font=("Arial", 15)).place(x=61, y=334)
Label(window, text="Others:", font=("Arial", 15)).place(x=61, y=376)

label_bill = Label(window, text="TOTAL BILL   (Rs):", font=("Arial", 15))
label_bill.place(x=61, y=502)

label_paid = Label(window, text="PAYMENT (Rs):", font=("Arial", 15))
label_paid.place(x=61, y=544)

label_balance = Label(window, text="BALANCE    (Rs):", font=("Arial", 15))
label_balance.place(x=61, y=586)

# Functions
def Add():
    total = num1.get() + num2.get() + num3.get() + num4.get() + num5.get() + num6.get() + num7.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(total))

def Diff():
    try:
        paid_amount = int(paidEntry.get())
        bill_amount = int(resultEntry.get())
        bal = paid_amount - bill_amount
        entry_balance.delete(0, END)
        entry_balance.insert(0, str(bal))
    except ValueError:
        entry_balance.delete(0, END)
        entry_balance.insert(0, "Invalid Input")

def Clr():
    for entry in [entry1, entry2, entry3, entry4, entry5, entry6, entry7, resultEntry, paidEntry, entry_balance]:
        entry.delete(0, END)

# Entries
entry1 = Entry(window, textvariable=num1)
entry1.place(x=300, y=125, height=25, width=143)

entry2 = Entry(window, textvariable=num2)
entry2.place(x=300, y=167, height=25, width=143)

entry3 = Entry(window, textvariable=num3)
entry3.place(x=300, y=209, height=25, width=143)

entry4 = Entry(window, textvariable=num4)
entry4.place(x=300, y=251, height=25, width=143)

entry5 = Entry(window, textvariable=num5)
entry5.place(x=300, y=293, height=25, width=143)

entry6 = Entry(window, textvariable=num6)
entry6.place(x=300, y=335, height=25, width=143)

entry7 = Entry(window, textvariable=num7)
entry7.place(x=300, y=377, height=25, width=143)

resultEntry = Entry(window)
resultEntry.place(x=300, y=503, height=25, width=143)

paidEntry = Entry(window)
paidEntry.place(x=300, y=545, height=25, width=143)

entry_balance = Entry(window)
entry_balance.place(x=300, y=586, height=25, width=143)

# Buttons
Button(window, text="BILL", fg="white", bg="green", font=("Arial", 14), command=Add).place(x=64, y=662, height=32, width=103)
Button(window, text="BALANCE", fg="white", bg="green", font=("Arial", 14), command=Diff).place(x=204, y=662, height=32, width=103)
Button(window, text="CLEAR", fg="white", bg="green", font=("Arial", 14), command=Clr).place(x=344, y=662, height=32, width=103)

window.mainloop()
