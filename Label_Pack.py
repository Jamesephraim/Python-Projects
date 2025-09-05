#label and pack concept in python tkinter
import tkinter
from tkinter import *

root=Tk()
root.geometry("400x250")
#root.resizable(False,False)
root.title("Label And Pack")

text_label=Label(text="HELLO WORLD",bg="red",fg="white",padx=100 ,pady=300 ,borderwidth=6,font="Sarif 20 bold")

text_label.pack( side="left" ,fill=X,anchor='w',pady=10)



root.mainloop()

