
#import tkinter

import tkinter as tk
from tkinter import *


def sum():
    num1=int(get1.get())
    num2=int(get2.get())
    add=num1+num2
    result["text"]=add
    
    
  

def sub():
    num1=int(get1.get())
    num2=int(get2.get())
    sub=num1-num2
    result["text"]=sub



def mul():
    num1=int(get1.get())
    num2=int(get2.get())
    mul=num1*num2
    result["text"]=mul


def div():
    num1=int(get1.get())
    num2=int(get2.get())
    res=int(num1/num2)
    result["text"]=res


    

win=tk.Tk()
win.title("Mini Calculator")
win.geometry("330x260")
win.resizable(False,False)





 

    
#Heading Text
head=tk.Label(text="Welcome to Mini Calculator")
head.place(x=90,y=30)



label=tk.Label(text="Enter two Number :")
label.place(x=10,y=80)

get1=tk.Entry(width=10)
get1.place(x=130,y=80)

get2=tk.Entry(width=10)
get2.place(x=202,y=80)

#+
btn=tk.Button(text="+",width=3,fg="white",bg="blue",command=sum)
btn.place(x=130,y=110)

#-
btn=tk.Button(text="-",width=3,fg="white",bg="blue",command=sub)
btn.place(x=165,y=110)

#*
btn=tk.Button(text="*",width=3,fg="white",bg="blue",command=mul)
btn.place(x=200,y=110)

#/
btn=tk.Button(text="/",width=3,fg="white",bg="blue",command=div)
btn.place(x=235,y=110)

result=tk.Label(font="arial 13 bold")
result.place(x=140,y=150)



win.mainloop()

