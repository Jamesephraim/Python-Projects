import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk


root=Tk()
root.geometry("500x400")
root.title('Image Viewer')

def showimg():
    filepath=filedialog.askopenfilename(filetypes=[("JPG","*.jpg"),("JPEG","*.jpeg"),("PNG","*.png")])
    img=Image.open(filepath)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img




frame=Frame(root)
frame.pack(side=BOTTOM,pady=10,padx=10)

lbl=Label(root)
lbl.pack()

btn1=Button(frame,text="Select Image",bg="blue",fg='orange',width=13,command=showimg)
btn1.pack(side=LEFT)

btn2=Button(frame,text="Exit",bg="red",fg='white',width=13,command=lambda:exit())
btn2.pack(padx=20)


root.mainloop()
