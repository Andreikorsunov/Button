from tkinter import *
from math import *

def lahe(event):
    if (a.get()!=""and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(0))/(2*a_),2)
            x2_=round((-1*b_+sqrt(0))/(2*a_),2)
            t=f"X1=(x1_), \nX2=(x2_)"
        elif D==0:
            x1_=(-1*b_)/(2*a_)
            t=f"X1=(x1_)"
        else:
            t="Корней нет"
        vastus.configure(text=f"D={D}\n(t)")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        elif b.get()=="":
            b.configure(bg="red")
        elif c.get()=="":
            c.configure(bg="red")


wind=Tk()
wind.geometry("700x300")
wind.title("Квадратные уравнения")
lbl=Label(wind,text="Решение квадратного уравнения",font="Calibri 26",fg="green",bg="lightblue")
lbl.pack()


a=Entry(wind,font="Calibri 26",fg="green",bg="lightblue",width=3)
a.pack(side=LEFT)
x1=Label(wind,text="x**2+",font="Calibri 26",fg="green")
x1.pack(side=LEFT)
b=Entry(wind,font="Calibri 26",fg="green",bg="lightblue",width=3)
b.pack(side=LEFT)
x2=Label(wind,text="x+",font="Calibri 26",fg="green")
x2.pack(side=LEFT)
c=Entry(wind,font="Calibri 26",fg="green",bg="lightblue",width=3)
c.pack(side=LEFT)
x3=Label(wind,text="=0",font="Calibri 26",fg="green")
x3.pack(side=LEFT)
vastus=Label(wind,text="Решение",height=4,width=60,bg="yellow")
vastus.pack(side=BOTTOM)

button=Button(wind,text="Решить",font="Calibri 26",bg="green")
button.pack(side=LEFT,padx=70)
button.bind("<Button-1>",lahe)

wind.mainloop()
