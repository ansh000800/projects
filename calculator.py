from  tkinter import *


root=Tk()
root.geometry("400x390")
root.title("Calculator anshul")
root.config(bg="black",)

equation=""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

label_result=Label(root,width=25,height=1,text="",font=("arial",40),bg="black",fg="white")
label_result.pack()
# button for no.1,2,3,4,5,6,7,8,9
Button(root,text="7",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("7"))).place(x=5,y=70)
Button(root,text="8",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("8"))).place(x=105,y=70)
Button(root,text="9",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("9"))).place(x=205,y=70)
Button(root,text="4",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("4"))).place(x=5,y=140)
Button(root,text="5",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("5"))).place(x=105,y=140)
Button(root,text="6",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("6"))).place(x=205,y=140)
Button(root,text="1",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("1"))).place(x=5,y=210)
Button(root,text="2",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("2"))).place(x=105,y=210)
Button(root,text="3",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("3"))).place(x=205,y=210)

# button for operations
Button(root,text="/",bd=1,width=5,height=1,font=("bold","20"),bg="grey",command=lambda: show(("/"))).place(x=305,y=70)
Button(root,text="*",bd=1,width=5,height=1,font=("bold","20"),bg="grey",command=lambda: show(("*"))).place(x=305,y=120)
Button(root,text="-",bd=1,width=5,height=1,font=("bold","20"),bg="grey",command=lambda: show(("-"))).place(x=305,y=170)
Button(root,text="+",bd=1,width=5,height=1,font=("bold","20"),bg="grey",command=lambda: show(("+"))).place(x=305,y=220)
Button(root,text="=",bd=2,width=5,height=2,font=("bold","20"),bg="red",command=lambda: calculate()).place(x=305,y=270)

# button for delete , dot and 0
Button(root,text=".",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("."))).place(x=5,y=280)
Button(root,text="0",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda: show(("0"))).place(x=105,y=280)
Button(root,text="C",bd=1,width=4,height=1,font=("bold","30"),bg="grey",command=lambda:clear()).place(x=205,y=280)








root.mainloop()