import tkinter as tk
import cv2
from PIL import Image,ImageTk

root=tk.Tk()

root.geometry('500x400')


label=tk.Label(root,width=400,height=350)
label.pack()

cap=cv2.VideoCapture(0)

def camara():
    ret,frame=cap.read()
    if ret:
        frame=cv2.resize(frame,(400,350))
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img=Image.fromarray(img)
        imgtk=ImageTk.PhotoImage(image=img)
        label.imgtk=imgtk
        label.configure(image=imgtk)
    root.after(10,camara)
camara()

root.mainloop()