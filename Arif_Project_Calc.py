from tkinter import *

# Syntax to create a Window
window = Tk()
window.title("Project_Calculator_BQ4") # To give the title of the window.
window.geometry("400x450") # To initialize the size of the window. 
window.resizable(False, False) # If you don't want to make your window resizable initialize this line. 

num1 = DoubleVar() # initialize the first variable
num2 = DoubleVar() # initialize the second variable


mainTitle = Label(window, text="Calculator", font=("Arial", 25))
mainTitle.place(x=134, y=45) # Use the place layout to place further labels

# Text
type1 = Label(window, text="Enter 1st No :", font=("Arial", 15))
type1.place(x=61, y=125)

type2 = Label(window, text="Enter 2nd No :", font=("Arial", 15))
type2.place(x=61, y=197)

resultLabel = Label(window, text="Result:", font=("Arial", 15))
resultLabel.place(x=118, y=336)

 # Use functions to give action to the button. 
def Add():
    sum = num1.get() + num2.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(sum))

def Diff():
    diff = num1.get() - num2.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(diff))

def Mul():
    mul = num1.get() * num2.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(mul))

def Div():
    div = num1.get() / num2.get()
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(div))

def Clr():
    entry1.delete(0, END)
    entry2.delete(0, END)
    resultEntry.delete(0, END)
    
    

# Entries Syntax
entry1 = Entry(window, textvariable=num1)
entry1.place(x=200, y=130, height=25, width=143)

entry2 = Entry(window, textvariable=num2)
entry2.place(x=200, y=202, height=25, width=143)

resultEntry = Entry(window)
resultEntry.place(x=200, y=340, height=25, width=143)

# Buttons syntax
buttonAdd = Button(window, text="+", fg="white", bg="green", font=("Arial", 14), command=Add) # Use command to call the functions.
buttonAdd.place(x=64, y=262, height=32, width=65)

buttonSub = Button(window, text="-", fg="white", bg="green", font=("Arial", 14), command=Diff)
buttonSub.place(x=134, y=262, height=32, width=65)

buttonMul = Button(window, text="x", fg="white", bg="green", font=("Arial", 14), command=Mul)
buttonMul.place(x=204, y=262, height=32, width=65)

buttonDiv = Button(window, text="/", fg="white", bg="green", font=("Arial", 14), command=Div) 
buttonDiv.place(x=274, y=262, height=32, width=65)


buttonClr = Button(window, text="Clr", fg="white", bg="green", font=("Arial", 14), command=Clr) 
buttonClr.place(x=135, y=400, height=32, width=143)


window.mainloop()


