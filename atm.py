from tkinter import *
from tkinter import messagebox
import random
import datetime as dt

date=dt.datetime.now()

Balance=1000000
root=Tk()
root.geometry("780x780")
root.title("ATM")
root.config(bg="grey")

account_no=Label(root,text="Account No.:",bg="grey",font="Bold")
account_no.place(x=10,y=10)

account=IntVar()
acc_no_insert=Entry(root,bg="grey",font="Bold",textvariable=account)
acc_no_insert.place(x=140,y=10)

amount=Label(root,text="Amount:",font="bold",bg="grey")
amount.place(x=10,y=70)

amount__i=IntVar()

amount_insert=Entry(root,bg="grey",font="bold",textvariable=amount__i)
amount_insert.place(x=100,y=70)


def checkamount():

    amount_i=int(amount__i.get())
    if(amount_i>0 and amount_i<=Balance):
        otp_insert.focus_set()
        messagebox.showinfo("OTP",OTP)
    else:
        if(amount_i<=0):
            messagebox.showwarning("Warning","Invalid amount.")
        elif(amount_i>Balance):
            messagebox.showwarning("Warning","Insufficient Balance.")




enter=Button(root,text="Enter",bg="silver",font="bold",command=checkamount)
enter.place(x=250,y=150)

OTP=random.randint(1000,9999)


Otp=Label(root,text="OTP:",bg="grey",font="bold")
Otp.place(x=10,y=250)

otp_i=IntVar()
otp_insert=Entry(root,bg="grey",font="bold",textvariable=otp_i)
otp_insert.place(x=70,y=250)

def check_otp():
    global Balance
    OTP_I=int(otp_i.get())
    if(OTP_I==OTP):
        Balance=Balance-int(amount__i.get())

        Rceipt=Label(root,text="Reciept",font=("Bold","25"),fg="purple")
        Rceipt.place(x=280,y=520)
        Date=Label(root,text=date,font=("bold","18"))
        Date.place(x=10,y=570)
        Line=Label(root,text=f"{amount__i.get()},is debited from {account.get()}",font=("bold","18"))
        Line.place(x=10,y=640)
        balance=Label(root,text=f"Available balance={Balance}",font=("bold","18"))
        balance.place(x=10,y=710)
    elif(OTP_I!=OTP):
        messagebox.showwarning("Warning","Invalid otp.")

submit=Button(root,text="Submit",bg="silver",font="bold",command=check_otp)
submit.place(x=250,y=400)

def Exit():
    root.destroy()

exit=Button(root,text="Exit",bg="grey",font="bold",command=Exit)
exit.pack(side="bottom")

root.mainloop()