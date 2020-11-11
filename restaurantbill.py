from tkinter import *
import random
import time
import datetime
import numbers
from tkinter import messagebox

root = Tk()
root.geometry("1350x650+0+0")
root.title("Restaurant Billing Management")

Tops = Frame(root, width=1350, height=50, bd=4, relief="raise")
Tops.pack(side=TOP)
Bottoms = Frame(root, width=1350, height=50, bd=4, relief="raise")
Bottoms.pack(side=BOTTOM)

f1 = Frame(root, width=900, height=650, bd=4, relief="raise")
f1.pack(side=LEFT)
f1a = Frame(f1, width=900, height=330, bd=4, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=4, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=430, bd=4, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=4, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=4, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=4, relief="raise")
f2ab.pack(side=LEFT)

f2 = Frame(root, width=440, height=650, bd=4, relief="raise")
f2.pack(side=RIGHT)

lblInfo = Label(Tops, font=('ALGERIAN', 25, 'bold'), text="Baby Panda Restaurant [Phoenix-Master]", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)


PaymentRef=StringVar()
FriedRice=StringVar()
ChickenRoll=StringVar()
Mojito=StringVar()
Coke=StringVar()
costFriedRice=StringVar()
costChickenRoll=StringVar()
costMojito=StringVar()
costCoke=StringVar()
dateRef=StringVar()
subTotal=StringVar()
vat=StringVar()
totalPrice=StringVar()
text_Input = StringVar()
dateRef.set(time.strftime("%d/%m/%y"))
operator = ""
vat.set(0)
FriedRice.set(0)
ChickenRoll.set(0)
Mojito.set(0)
Coke.set(0)
subTotal.set(0)
totalPrice.set(0)
costFriedRice.set(150)
costChickenRoll.set(40)
costMojito.set(60)
costCoke.set(55)


def tPrice():
    cBprice=int(costFriedRice.get())
    bBprice=int(costChickenRoll.get())
    fFprice=int(costMojito.get())
    sDprice=int(costCoke.get())

    cBno=int(FriedRice.get())
    bBno=int(ChickenRoll.get())
    fFno=int(Mojito.get())
    sDno=int(Coke.get())
    tempVat=int(vat.get())
    subPrice=(cBprice*cBno+bBprice*bBno+fFprice*fFno+sDprice*sDno)
    totalCost=str('%d'%subPrice),"Rs"
    totalCostwithVat=str('%d'%(subPrice +(subPrice*tempVat)/100)),"Rs"
    subTotal.set(totalCost)
    totalPrice.set(totalCostwithVat)


def iExit():
    qexit= messagebox.askyesno("Billing System", "Do you want to exit?")
    if qexit>0:
        root.destroy()
        return

def reset():
    PaymentRef.set("")
    FriedRice.set(0)
    ChickenRoll.set(0)
    Mojito.set(0)
    Coke.set(0)
    subTotal.set(0)
    totalPrice.set(0)

def refNo():
    x =  random.randint(10202, 45671)
    randomRef= str(x)
    PaymentRef.set("BILL"+randomRef)

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(f2, font=('arial', 10, 'bold'), textvariable=text_Input, bd=40, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="7",
              command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="8",
              command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="9",
              command=lambda: btnClick(9)).grid(row=1, column=2)
btnPlus = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="+",
                 command=lambda: btnClick("+")).grid(row=1, column=3)

btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="4",
              command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="5",
              command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="6",
              command=lambda: btnClick(6)).grid(row=2, column=2)
btnSub = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="-",
                command=lambda: btnClick("-")).grid(row=2, column=3)

btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="1",
              command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="2",
              command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="3",
              command=lambda: btnClick(3)).grid(row=3, column=2)
btnMult = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="*",
                 command=lambda: btnClick("*")).grid(row=3, column=3)

btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="0",
              command=lambda: btnClick(0)).grid(row=4, column=0)
btnClear = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="C",
                  command=btnClearDisplay).grid(row=4, column=1)
btnEquals = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="=",
                   command=btnEqualsInput).grid(row=4, column=2)
btnDiv = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="/",
                command=lambda: btnClick("/")).grid(row=4, column=3)

lblRef=Label(f1aa,font=('Arial Black',12,'bold'),fg="green",text="Reference No", bd=16, justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa,font=('Arial Black',12,'bold'),textvariable=PaymentRef, bd=10,insertwidth=2, justify='left')
txtRef.grid(row=0,column=1)

lblCb=Label(f1aa,font=('Arial Black',12,'bold'),text="Fried Rice", bd=16, justify='left')
lblCb.grid(row=1,column=0)
txtCb=Entry(f1aa,font=('Arial Black',12,'bold'),textvariable=FriedRice, bd=10,insertwidth=2, justify='left')
txtCb.grid(row=1,column=1)

lblBb=Label(f1aa,font=('Arial Black',12,'bold'),text="Chicken Roll", bd=16, justify='left')
lblBb.grid(row=2,column=0)
txtBb=Entry(f1aa,font=('Arial Black',12,'bold'),textvariable=ChickenRoll, bd=10,insertwidth=2, justify='left')
txtBb.grid(row=2,column=1)

lblFf=Label(f1aa,font=('Arial Black',12,'bold'),text="Mojito", bd=16, justify='left')
lblFf.grid(row=3,column=0)
txtFf=Entry(f1aa,font=('Arial Black',12,'bold'),textvariable=Mojito, bd=10,insertwidth=2, justify='left')
txtFf.grid(row=3,column=1)

lblSd=Label(f1aa,font=('Arial Black',12,'bold'),text="Coke", bd=16, justify='left')
lblSd.grid(row=4,column=0)
txtSd=Entry(f1aa,font=('Arial Black',12,'bold'),textvariable=Coke, bd=10,insertwidth=2, justify='left')
txtSd.grid(row=4,column=1)

lbldate=Label(f1ab,font=('Arial Black',16,'bold'),text="Date", bd=16, justify='right')
lbldate.grid(row=0,column=0)
txtdate=Entry(f1ab,font=('Arial Black',16,'bold'),textvariable=dateRef, bd=10,insertwidth=2, justify='right')
txtdate.grid(row=0,column=1)

lblCcb=Label(f1ab,font=('Arial Black',12,'bold'),text="Price of Fried Rice", bd=16, justify='right')
lblCcb.grid(row=1,column=0)
txtCcb=Entry(f1ab,font=('Arial Black',12,'bold'),textvariable=costFriedRice, bd=10,insertwidth=2, justify='left')
txtCcb.grid(row=1,column=1)

lblCbb=Label(f1ab,font=('Arial Black',12,'bold'),text="Price of Chicken Roll", bd=16, justify='left')
lblCbb.grid(row=2,column=0)
txtCbb=Entry(f1ab,font=('Arial Black',12,'bold'),textvariable=costChickenRoll, bd=10,insertwidth=2, justify='left')
txtCbb.grid(row=2,column=1)

lblCff=Label(f1ab,font=('Arial Black',12,'bold'),text="Price of Mojito", bd=16, justify='left')
lblCff.grid(row=3,column=0)
txtCff=Entry(f1ab,font=('Arial Black',12,'bold'),textvariable=costMojito, bd=10,insertwidth=2, justify='left')
txtCff.grid(row=3,column=1)

lblCsd=Label(f1ab,font=('Arial Black',12,'bold'),text="Price of coke", bd=16, justify='left')
lblCsd.grid(row=4,column=0)
txtCsd=Entry(f1ab,font=('Arial Black',12,'bold'),textvariable=costCoke, bd=10,insertwidth=2, justify='left')
txtCsd.grid(row=4,column=1)

lblPrice=Label(f2aa,font=('Arial black',16,'bold'),text="Price", bd=16, justify='left')
lblPrice.grid(row=0,column=0)
txtPrice=Entry(f2aa,font=('Arial Black',16,'bold'),textvariable=subTotal, bd=10,insertwidth=2, justify='left')
txtPrice.grid(row=0,column=1)

lblVat=Label(f2aa,font=('Arial Black',16,'bold'),text="VAT", bd=16, justify='left')
lblVat.grid(row=1,column=0)
txtVat=Entry(f2aa,font=('Arial Black',16,'bold'),textvariable=vat, bd=10,insertwidth=2, justify='left')
txtVat.grid(row=1,column=1)

lblTp=Label(f2aa,font=('Arial Black',16,'bold'),text="Total Price", bd=16, justify='left')
lblTp.grid(row=2,column=0)
txtTp=Entry(f2aa,font=('Arial Black',16,'bold'),textvariable=totalPrice, bd=10,insertwidth=2, justify='left')
txtTp.grid(row=2,column=1)

btnTotal=Button(f2ab,padx=16,pady=16,bd=8, fg="black",font=('Arial Black',16,'bold'),width=15,
                text="Total Price",command=tPrice).grid(row=0,column=0)
btnRefer=Button(f2ab,padx=16,pady=16,bd=8, fg="green",font=('Arial Black',16,'bold'),width=15,
                text="Sales Reference",command=refNo).grid(row=0,column=1)
btnReset=Button(f2ab,padx=16,pady=16,bd=8, fg="blue",font=('Arial Black',16,'bold'),width=15,
                text="Reset",command=reset).grid(row=1,column=0)
btnExit=Button(f2ab,padx=16,pady=16,bd=8, fg="red",font=('Arial Black',16,'bold'),width=15,
                text="Exit",command=iExit).grid(row=1,column=1)

root.mainloop()
