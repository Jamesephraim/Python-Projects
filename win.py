import tkinter
from tkinter import *
root = tkinter.Tk()
 

#Submit Function

 

#width and height
root.geometry("400x300")
#bg color
#root.configure(bg="#ADD8E6")

#title of box
root.title("Student Login Form")


#label box
one=tkinter.Label(root,text="Enter First Number :",fg="blue",font=("Arial",10)).pack( )#anchor=tkinter.W,padx=10
#name.grid(row=2,column=2,padx=5,pady=5)
#Input box
one=tkinter.Entry(root,width=30,fg="blue").pack( )
first=StringVar()       #IntVar(),DoubleVar(),StringVar()

#name.insert(0,"Enter Name :")
#label box
two=tkinter.Label(root,text="Enter Your Email :",fg="blue",font=("Arial",10)).pack()
#Input box
two=tkinter.Entry(root,width=30,fg="blue").pack()

#def myfun():

#Submit button
submit_btn=tkinter.Button(root,text="Submit" ).pack( )
#submit_btn.grid(row=3,column=1,sticky=W)

emptylabel=Label(root,fg="blue")
root.mainloop()
