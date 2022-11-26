import tkinter as tk # i am importing my tkinter module
from tkinter import* # im importing everything from tkinter module

top=Tk() # creating tkinter window
top.title("EB Bill Amount Calculator")
top.geometry("600x600")# used to set dimensions of it

unit= StringVar()
amount=StringVar()

# Create Button and add some text
#button = Button(root, text = 'Geeks')
#button.pack(side = TOP, pady = 5)

def calculate():
    units=int(unit.get())
    billamount=0
    if units>=1 and units<=100:
        billamount=units*1
    elif units>=101 and units<=200:
        billamount=4.50*(units)+2.50
    elif units>=101 and units<=200:
        billamount=4.50*(units)+4.50
    elif units>=101 and units<=200:
        billamount=6.00*(units)+6.0

    amount.set("Rs: "+str(billamount))


  
label1=Label(top,text="Enter the unit you consumed: ").place(x=10,y=30)
entry1=Entry(top,textvariable=unit,).place(x=220,y=30)
btn1 = Button(top,text = "Calculate",command = calculate).place(x=250,y=60)

lable2 = Label(top,text = "Bill amount : ").place(x =20,y=90)
entry2 = Entry(top,textvariable = amount).place(x=220,y=90)

top.mainloop() # execute tkinter