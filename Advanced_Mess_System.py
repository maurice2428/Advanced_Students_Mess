from tkinter import*
import random
import time;
import datetime
import tkinter.messagebox


root = Tk()
root.geometry("1350x750+0+0")
root.title("AdvdMess-Jaramogi Oginga Odinga Univerity of Science and Technology")
root.configure(background = '#dcdcdc')


Tops = Frame(root, bg='#fffafa', bd=10,pady=5, relief=RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('Times New Roman',40,'bold'), text="  Advanced Jooust Students' Mess  System \t", bd=20, bg='#c0c0c0',fg='#708090')
lblTitle.grid(row=0, column=0)



ReceiptCal_F = Frame(root, bd=5, relief= RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F = Frame(ReceiptCal_F,bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F = Frame(ReceiptCal_F,bd=4,relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F = Frame(ReceiptCal_F,bd=2,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

Menuframe = Frame(root, bd=5, bg='#fffafa',relief= RIDGE)
Menuframe.pack(side=LEFT)
Cost_F = Frame(Menuframe,bd=2)
Cost_F.pack(side=BOTTOM)
Drinks_F = Frame(Menuframe,bd=5)
Drinks_F.pack(side=TOP)


Drinks_F = Frame(Menuframe,bd=5, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F = Frame(Menuframe, relief=RIDGE)
Cake_F.pack(side=RIGHT)
#================================Variable====================================================================================================================================

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()  
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var13 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Soda = StringVar()
E_Milk = StringVar()
E_Water = StringVar()
E_Tea = StringVar()
E_Coffee = StringVar()
E_Ugali = StringVar()
E_Cabbage = StringVar()
E_Kales = StringVar()

E_Maandazi = StringVar()
E_Rice = StringVar()
E_Pilau = StringVar()
E_Githeri = StringVar()
E_Nyama = StringVar()
E_Matumbo = StringVar()
E_Beans = StringVar()
E_Ndengu = StringVar()

E_Soda.set("0")
E_Milk.set("0")
E_Water.set("0")
E_Tea.set("0")
E_Coffee.set("0")
E_Ugali.set("0")
E_Cabbage.set("0")
E_Kales.set("0")


E_Maandazi.set("0")
E_Rice.set("0")
E_Pilau.set("0")
E_Githeri.set("0")
E_Nyama.set("0")
E_Matumbo.set("0")
E_Beans.set("0")
E_Ndengu.set("0")


DateofOrder.set(time.strftime("%d/%m/%Y"))
#============================Function Declaration==================================================================================================================================
def iExit():
    iExit = tkinter.messagebox.askyesno("Terminate System","Confirm If You Want To Exit?")
    if iExit > 0:
        root.destroy()
        return
    
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0" ,END)
    
    E_Soda.set("0")
    E_Milk.set("0")
    E_Water.set("0")
    E_Tea.set("0")
    E_Coffee.set("0")
    E_Ugali.set("0")
    E_Cabbage.set("0")
    E_Kales.set("0")
    E_Maandazi.set("0")
    E_Rice.set("0")
    E_Pilau.set("0")
    E_Githeri.set("0")
    E_Nyama.set("0")
    E_Matumbo.set("0")
    E_Beans.set("0")
    E_Ndengu.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)  
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)    
    var14.set(0)
    var13.set(0)
    var16.set(0)

def CostofItem():
    Item1 = float(E_Soda.get())
    Item2 = float(E_Milk.get())
    Item3 = float(E_Water.get())
    Item4 = float(E_Tea.get())
    Item5 = float(E_Coffee.get())
    Item6 = float(E_Ugali.get())
    Item7 = float(E_Cabbage.get())
    Item8 = float(E_Kales.get())
    
    Item9 = float(E_Maandazi.get())
    Item10 = float(E_Rice.get())
    Item11 = float(E_Pilau.get())
    Item12 = float(E_Githeri.get())
    Item13 = float(E_Nyama.get())
    Item14 = float(E_Matumbo.get())
    Item13 = float(E_Beans.get())
    Item16 = float(E_Ndengu.get())
    
    
    PriceofDrinks = (Item1*30)+(Item2*30)+(Item3*20)+(Item4*10)+(Item5*5)
    PriceofFood = (Item6*10)+(Item7*5)+(Item8*5)+(Item9*10)+(Item10*10)+(Item11*20)+(Item12*20)+(Item13*30)+(Item14*20)+(Item13*10)+(Item16*13)
    
    DrinksPrice = "Kshs", str('%.2f'%(PriceofDrinks))
    FoodPrice = "Kshs", str("%.2f"%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Kshs", str('%.2f'%(1.5))
    ServiceCharge.set(SC)
    
    SubTotalofITEMS = "Kshs", str("%.2f"%(PriceofDrinks + PriceofFood + 1.5))
    SubTotal.set(SubTotalofITEMS)
    
    Tax = "Kshs", str("%.2f"%((PriceofDrinks + PriceofFood + 1.5)*0.005))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofFood + 1.5)*0.13)
    TC = "Kshs", str("%.2f"%(PriceofDrinks + PriceofFood + 1.5 +TT))
    TotalCost.set(TC)
    
def chkSoda():
    if (var1.get() == 1):
        txtSoda.configure(state = NORMAL)
        txtSoda.focus()
        txtSoda.delete('0', END)
        E_Soda.set("")
    elif var1.get() == 0:
        txtSoda.configure(state = DISABLED)
        E_Soda.set("0")
    
def chkEspesso():
    if (var2.get() == 1):
        txtMilk.configure(state = NORMAL)
        txtMilk.focus()
        txtMilk.delete('0', END)
        E_Milk.set("")
    elif var2.get() == 0:
        txtMilk.configure(state = DISABLED)
        E_Milk.set("0")

def chkWater():
    if (var3.get() == 1):
        txtWater.configure(state = NORMAL)
        txtWater.focus()
        txtWater.delete('0', END)
        E_Water.set("")
    elif var3.get() == 0:
        txtWater.configure(state = DISABLED)
        E_Water.set("0")   

def chkTea():
    if (var4.get() == 1):
        txtTea.configure(state = NORMAL)
        txtTea.focus()
        txtTea.delete('0', END)
        E_Tea.set("")
    elif var4.get() == 0:
        txtTea.configure(state = DISABLED)
        E_Tea.set("0") 
        
def chkCoffee():
    if (var5.get() == 1):
        txtCoffee.configure(state = NORMAL)
        txtCoffee.focus()
        txtCoffee.delete('0', END)
        E_Coffee.set("")
    elif var5.get() == 0:
        txtCoffee.configure(state = DISABLED)
        E_Coffee.set("0") 
        
def chkUgali():
    if (var6.get() == 1):
        txtUgali.configure(state = NORMAL)
        txtUgali.focus()
        txtUgali.delete('0', END)
        E_Ugali.set("")
    elif var6.get() == 0:
        txtUgali.configure(state = DISABLED)
        E_Ugali.set("0")

def chkCabbage():
    if (var7.get() == 1):
        txtCabbage.configure(state = NORMAL)
        txtCabbage.focus()
        txtCabbage.delete('0', END)
        E_Cabbage.set("")
    elif var7.get() == 0:
        txtCabbage.configure(state = DISABLED)
        E_Cabbage.set("0")

def chkKales():
    if (var8.get() == 1):
        txtKales.configure(state = NORMAL)
        txtKales.focus()
        txtKales.delete('0', END)
        E_Kales.set("")
    elif var8.get() == 0:
        txtKales.configure(state = DISABLED)
        E_Kales.set("0")        

def chkMaandazi():
    if (var9.get() == 1):
        txtMaandazi.configure(state = NORMAL)
        txtMaandazi.focus()
        txtMaandazi.delete('0', END)
        E_Maandazi.set("")
    elif var9.get() == 0:
        txtMaandazi.configure(state = DISABLED)
        E_Maandazi.set("0")
    
def chkRice():
    if (var10.get() == 1):
        txtRice.configure(state = NORMAL)
        txtRice.focus()
        txtRice.delete('0', END)
        E_Rice.set("")
    elif var10.get() == 0:
        txtRice.configure(state = DISABLED)
        E_Rice.set("0")

def chkPilau():
    if (var11.get() == 1):
        txtPilau.configure(state = NORMAL)
        txtPilau.focus()
        txtPilau.delete('0', END)
        E_Pilau.set("")
    elif var11.get() == 0:
        txtPilau.configure(state = DISABLED)
        E_Pilau.set("0")   

def chkGitheri():
    if (var12.get() == 1):
        txtGitheri.configure(state = NORMAL)
        txtGitheri.focus()
        txtGitheri.delete('0', END)
        E_Githeri.set("")
    elif var12.get() == 0:
        txtGitheri.configure(state = DISABLED)
        E_Githeri.set("0") 
        
def chkNyama():
    if (var13.get() == 1):
        txtNyama.configure(state = NORMAL)
        txtNyama.focus()
        txtNyama.delete('0', END)
        E_Nyama.set("")
    elif var13.get() == 0:
        txtNyama.configure(state = DISABLED)
        E_Nyama.set("0") 
        
def chkMatumbo():
    if (var14.get() == 1):
        txtMatumbo.configure(state = NORMAL)
        txtMatumbo.focus()
        txtMatumbo.delete('0', END)
        E_Matumbo.set("")
    elif var14.get() == 0:
        txtMatumbo.configure(state = DISABLED)
        E_Matumbo.set("0")

def chkBeans ():
    if (var13.get() == 1):
        txtBeans.configure(state = NORMAL)
        txtBeans.focus()
        txtBeans.delete('0', END)
        E_Beans.set("")
    elif var13.get() == 0:
        txtBeans.configure(state = DISABLED)
        E_Beans.set("0")

def chkNdengu():
    if (var16.get() == 1):
        txtNdengu.configure(state = NORMAL)
        txtNdengu.focus()
        txtNdengu.delete('0', END)
        E_Ndengu.set("")
    elif var16.get() == 0:
        txtNdengu.configure(state = DISABLED)
        E_Ndengu.set("0")


def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10903, 609235)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)
    
    txtReceipt.insert(END, "Receipt Ref:\t\t\t" + Receipt_Ref.get() + '\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, "Items:\t\t\t\t" + "Cost of Items \n")
    txtReceipt.insert(END, "Soda:\t\t\t\t\t" + E_Soda.get() + "\n")
    txtReceipt.insert(END, "Milk:\t\t\t\t\t" + E_Milk.get() + "\n")
    txtReceipt.insert(END, "Water:\t\t\t\t\t" + E_Water.get() + "\n")
    txtReceipt.insert(END, "Tea:\t\t\t\t\t" + E_Tea.get() + "\n")
    txtReceipt.insert(END, "Coffee:\t\t\t\t\t" + E_Coffee.get() + "\n")
    txtReceipt.insert(END, "Ugali:\t\t\t\t\t" + E_Ugali.get() + "\n")
    txtReceipt.insert(END, "Cabbage:\t\t\t\t\t" + E_Cabbage.get() + "\n")
    txtReceipt.insert(END, "Kales:\t\t\t\t\t" + E_Kales.get() + "\n")
    txtReceipt.insert(END, "Maandazi:\t\t\t\t\t" + E_Maandazi.get() + "\n")
    txtReceipt.insert(END, "Rice:\t\t\t\t\t" + E_Rice.get() + "\n")
    txtReceipt.insert(END, "Pilau:\t\t\t\t\t" + E_Pilau.get() + "\n")
    txtReceipt.insert(END, "Githeri:\t\t\t\t\t" + E_Githeri.get() + "\n")
    txtReceipt.insert(END, "Nyama:\t\t\t\t\t" + E_Nyama.get() + "\n")
    txtReceipt.insert(END, "Matumbo:\t\t\t\t\t" + E_Matumbo.get() + "\n")
    txtReceipt.insert(END, "Beans:\t\t\t\t\t" + E_Beans.get() + "\n")
    txtReceipt.insert(END, "Ndengu:\t\t\t\t\t" + E_Ndengu.get() + "\n")
    
    txtReceipt.insert(END, "Cost Of Food:\t\t\t\t" + CostofDrinks.get() + "\nTax Paid:\t\t\t\t" + PaidTax.get() + "\n")
    txtReceipt.insert(END, "Cost Of Drinks:\t\t\t\t" + CostofFood.get() + "\nSubTotal:\t\t\t\t" + str(SubTotal.get()) + "\n")
    txtReceipt.insert(END, "Service Charge:\t\t\t\t" + ServiceCharge.get() + "\nTotal Cost: \t\t\t\t" + str(TotalCost.get())+ "\n")
    
    
    


#=================================Drinks====================================================================================================================
Soda = Checkbutton(Drinks_F, text="SODA", variable=var1,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'),command = chkSoda).grid(row=0, sticky='w')
Milk = Checkbutton(Drinks_F, text="MILK", variable=var2,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'), command = chkEspesso).grid(row=1, sticky='w')
Water = Checkbutton(Drinks_F, text="WATER", variable=var3,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'), command = chkWater).grid(row=2, sticky='w')
Tea = Checkbutton(Drinks_F, text="TEA", variable=var4,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'), command = chkTea).grid(row=3, sticky='w')
Coffee = Checkbutton(Drinks_F, text="COFFEE", variable=var5,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'), command = chkCoffee).grid(row=4, sticky='w')
Ugali = Checkbutton(Drinks_F, text="UGALI", variable=var6,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'), command = chkUgali).grid(row=5, sticky='w')
Cabbage = Checkbutton(Drinks_F, text="CABBAGE", variable=var7,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'), command = chkCabbage).grid(row=6, sticky='w')
Kales = Checkbutton(Drinks_F, text="KALES", variable=var8,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'), command = chkKales).grid(row=7 , sticky='w')
#=================================Entry Box for Drinks====================================================================================================================
txtSoda = Entry(Drinks_F, font=('Times New Roman',14,'bold'), textvariable = E_Soda,bd=8, width=22, justify=LEFT, state= DISABLED)
txtSoda.grid(row=0, column=1)
txtMilk = Entry(Drinks_F, font=('Times New Roman',14,'bold'), textvariable = E_Milk,bd=8, width=22, justify=LEFT, state= DISABLED)
txtMilk.grid(row=1, column=1)
txtWater = Entry(Drinks_F, font=('Times New Roman',14,'bold'), textvariable = E_Water,bd=8, width=22, justify=LEFT, state= DISABLED)
txtWater.grid(row=2, column=1)

txtTea = Entry(Drinks_F, font=('Times New Roman',14,'bold'), textvariable = E_Tea, bd=8, width=22, justify=LEFT, state= DISABLED)
txtTea.grid(row=3, column=1)
txtCoffee = Entry(Drinks_F, font=('Times New Roman',14,'bold'), textvariable = E_Coffee,bd=8, width=22, justify=LEFT, state= DISABLED)
txtCoffee.grid(row=4, column=1)
txtUgali = Entry(Drinks_F, font=('Times New Roman',14,'bold'), textvariable = E_Ugali, bd=8, width=22, justify=LEFT, state= DISABLED)
txtUgali.grid(row=5, column=1)

txtCabbage = Entry(Drinks_F, font=('Times New Roman',14,'bold'),textvariable = E_Cabbage, bd=8, width=22, justify=LEFT, state= DISABLED)
txtCabbage.grid(row=6, column=1)
txtKales = Entry(Drinks_F, font=('Times New Roman',14,'bold'), textvariable = E_Kales, bd=8, width=22, justify=LEFT, state= DISABLED)
txtKales.grid(row=7, column=1)
#=================================Food====================================================================================================================
Maandazi = Checkbutton(Cake_F, text="MAANDAZI", variable=var9,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'),command = chkMaandazi).grid(row=0, sticky='w')
Rice = Checkbutton(Cake_F, text="RICE", variable=var10,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'),command = chkRice).grid(row=1, sticky='w')
Pilau = Checkbutton(Cake_F, text="PILAU", variable=var11,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'),command = chkPilau).grid(row=2, sticky='w')
Githeri = Checkbutton(Cake_F, text="GITHERI", variable=var12,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'),command = chkGitheri).grid(row=3, sticky='w')
Nyama = Checkbutton(Cake_F, text="NYAMA", variable=var13,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'),command = chkNyama).grid(row=4, sticky='w')
Matumbo = Checkbutton(Cake_F, text="MATUMBO", variable=var14,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'),command = chkMatumbo).grid(row=5, sticky='w')
Beans = Checkbutton(Cake_F, text="BEANS", variable=var13,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'),command = chkBeans).grid(row=6, sticky='w')
Ndengu = Checkbutton(Cake_F, text="NDENGU", variable=var16,onvalue=1,offvalue=0,font=('Times New Roman',13,'bold'),command = chkNdengu).grid(row=7 , sticky='w')
#===============================Entry Box for Food====================================================================================================================
txtMaandazi = Entry(Cake_F, font=('Times New Roman',14,'bold'), textvariable= E_Maandazi,bd=8, width=22, justify=LEFT, state= DISABLED)
txtMaandazi.grid(row=0, column=1)
txtRice = Entry(Cake_F, font=('Times New Roman',14,'bold'),textvariable = E_Rice,bd=8, width=22, justify=LEFT, state= DISABLED)
txtRice.grid(row=1, column=1)
txtPilau = Entry(Cake_F, font=('Times New Roman',14,'bold'),textvariable = E_Pilau,bd=8, width=22, justify=LEFT, state= DISABLED)
txtPilau.grid(row=2, column=1)
txtGitheri = Entry(Cake_F, font=('Times New Roman',14,'bold'),textvariable = E_Githeri,bd=8, width=22, justify=LEFT, state= DISABLED)
txtGitheri.grid(row=3, column=1)
txtNyama = Entry(Cake_F, font=('Times New Roman',14,'bold'),textvariable = E_Nyama,bd=8, width=22, justify=LEFT, state= DISABLED)
txtNyama.grid(row=4, column=1)
txtMatumbo = Entry(Cake_F, font=('Times New Roman',14,'bold'),textvariable = E_Matumbo,bd=8, width=22, justify=LEFT, state= DISABLED)
txtMatumbo.grid(row=5, column=1)
txtBeans = Entry(Cake_F, font=('Times New Roman',14,'bold'), textvariable = E_Beans,bd=8, width=22, justify=LEFT, state= DISABLED)
txtBeans.grid(row=6, column=1)
txtNdengu = Entry(Cake_F, font=('Times New Roman',14,'bold'),textvariable = E_Ndengu,bd=8, width=22, justify=LEFT, state= DISABLED)
txtNdengu.grid(row=7, column=1)
#==================================Total Cost====================================================================================================================================
lblCostofDrinks = Label(Cost_F, font=('Times New Roman',14,'bold'),text="Cost of Food\t",fg="black")
lblCostofDrinks.grid(row=0, column=0, sticky='w')
textCostofDrinks = Entry(Cost_F,font=('Times New Roman',14,'bold'), textvariable =CostofFood , bd=7,bg='white',insertwidth=2, justify=RIGHT,fg='black')
textCostofDrinks.grid(row=0, column=1)

lblCostofFood = Label(Cost_F, font=('Times New Roman',14,'bold'),text="Cost of Drinks",fg="black")
lblCostofFood.grid(row=1, column=0, sticky='w')
textCostofFood = Entry(Cost_F,font=('Times New Roman',14,'bold'), textvariable = CostofDrinks, bd=7,bg='white',insertwidth=2, justify=RIGHT,fg='black')
textCostofFood.grid(row=1, column=1)

lblServiceCharge = Label(Cost_F, font=('Times New Roman',14,'bold'),text="Service Charge",fg="black")
lblServiceCharge.grid(row=2, column=0, sticky='w')
textServiceCharge = Entry(Cost_F,font=('Times New Roman',14,'bold'), textvariable = ServiceCharge, bd=7,bg='white',insertwidth=2, justify=RIGHT,fg='black')
textServiceCharge.grid(row=2, column=1)
#==================================Payment Information====================================================================================================================================
lblPaidTax = Label(Cost_F, font=('Times New Roman',14,'bold'),text="\tPaid Tax\t",fg="black")
lblPaidTax.grid(row=0, column=2, sticky='w')
textPaidTax = Entry(Cost_F,font=('Times New Roman',14,'bold'), textvariable = PaidTax, bd=7,bg='white',insertwidth=2, justify=RIGHT,fg='black')
textPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F, font=('Times New Roman',14,'bold'),text="\tSub Total",fg="black")
lblSubTotal.grid(row=1, column=2, sticky='w')
textSubTotal = Entry(Cost_F,font=('Times New Roman',14,'bold'), textvariable = SubTotal, bd=7,bg='white',insertwidth=2, justify=RIGHT,fg='black')
textSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F, font=('Times New Roman',14,'bold'),text="\tTotal Cost  ",fg="black")
lblTotalCost.grid(row=2, column=2, sticky='w')
textTotalCost = Entry(Cost_F,font=('Times New Roman',14,'bold'), textvariable = TotalCost, bd=7,bg='white',insertwidth=2, justify=RIGHT,fg='black')
textTotalCost.grid(row=2, column=3)
#===================================Receipt====================================================================================================================================

txtReceipt = Text(Receipt_F,width=46, height=12, bg='white', bd=4, font=('Times New Roman',12,'bold'),fg='black') 
txtReceipt.grid(row=0, column=0)
#===================================Buttons===================================================================================================================================
btnTotal = Button(Buttons_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="Total", command = CostofItem).grid(row=0, column=0)
btnTReceipt = Button(Buttons_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="Receipt", command = Receipt).grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="Reset", command= Reset).grid(row=0, column=2)
btnExit = Button(Buttons_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="Exit",command= iExit).grid(row=0, column=3)
#===================================Calculator Display====================================================================================================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator) 

def btnClear():
    global operator
    operator = ""
    text_Input.set("")


def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""    

txtDisplay = Entry(Cal_F,width=45, bg='white', bd=4, font=('Times New Roman',12,'bold'),justify=RIGHT, textvariable=text_Input,fg='black') 
txtDisplay.grid(row=0, column=0,columnspan=4,pady=1)
txtDisplay.insert(0, "0")
#===================================Calculator Buttons===================================================================================================================================
btn7 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="7",bg='#fff5ee', command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="8",bg='#fff5ee',command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="9",bg='#fff5ee',command=lambda: btnClick(9)).grid(row=2, column=2)
btnAdd = Button(Cal_F , padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="+",bg='#fff5ee',command=lambda: btnClick("+")).grid(row=2, column=3)
#===================================Calculator Buttons===================================================================================================================================
btn4 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="4",bg='#fff5ee',command=lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="5",bg='#fff5ee',command=lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="6",bg='#fff5ee',command=lambda:btnClick(6)).grid(row=3, column=2)
btnSub = Button(Cal_F , padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="-",bg='#fff5ee',command=lambda:btnClick("-")).grid(row=3, column=3)
#===================================Calculator Buttons===================================================================================================================================
btn1 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="1",bg='#fff5ee',command=lambda:btnClick(1)).grid(row=4, column=0)
btn2 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="2",bg='#fff5ee',command=lambda:btnClick(2)).grid(row=4, column=1)
btn3 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="3",bg='#fff5ee',command=lambda:btnClick(3)).grid(row=4, column=2)
btnMulti = Button(Cal_F , padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="*",bg='#fff5ee',command=lambda:btnClick("*")).grid(row=4, column=3)
#===================================Calculator Buttons===================================================================================================================================
btn0 = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="0",bg='#fff5ee',command=lambda:btnClick(0)).grid(row=5, column=0)
btnClear = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="C",bg='#fff5ee',command= btnClear).grid(row=5, column=1)
btnEquals = Button(Cal_F, padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="=",bg='#fff5ee',command= btnEquals).grid(row=5, column=2)
btnDiv = Button(Cal_F , padx=16,pady=1, bd=7,fg='black', font=('Times New Roman',16,'bold'), width=4, text="/",bg='#fff5ee',command=lambda:btnClick("/")).grid(row=5, column=3)

root.mainloop( )