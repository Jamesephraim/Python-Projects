import tkinter as tk
from tkinter import messagebox,ttk





root=tk.Tk()
root.geometry('300x300')
def asdf():
    x=gender.get()
    print(x)

choices=['Male','Female','Others']
gender=ttk.Combobox(root,values=choices,height=2)
gender.pack()
 
btn=tk.Button(root,text='button',command=asdf)
btn.pack()
 

root.mainloop()
