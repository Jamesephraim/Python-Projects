import socket
from  tkinter import *
from tkinter import filedialog,messagebox
import os





root=Tk()

root.title('EJ')

root.geometry("400x460")
root.resizable(False,False)



heading=Label(root,text='File Transfer',width=24,font="arial 20 bold",bg="#ddd")
heading.place(x=0,y=0)


f1=Frame(root,width=400,height=200,bg='blue')
f1.place(x=0,y=38)


send=Button(f1,text='Send',bg='orange',height=3,width=10)
send.place(x=40,y=30)

receive=Button(f1,text='Receive',bg='orange',height=3,width=10)
receive.place(x=280,y=30)
 
bg=PhotoImage()












root.mainloop()
