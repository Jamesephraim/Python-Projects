#from tkinter import *
import tkinter as tk
import cv2
from PIL import Image,ImageTk

global name
win=tk.Tk()
win.geometry('400x500')
frame=tk.Frame(win)
frame.pack()

label=tk.Label(frame,width=200,height=200)
label.pack()

 
    
cap=cv2.VideoCapture(0)
print(cap.isOpened())
def update_frame():
   while cap.isOpened():
    ret, frame=cap.read()
    if ret:
        frame=cv2.resize(frame,(200,200))
        img=Image.fromarray(frame)
        imgtk=ImageTk.PhotoImage(image=img)
        label.imgtk=imgtk
        label.configure(image=imgtk)
    #window.after(10,update_frame)
    name="Jammi"
    cv2.imshow('Window',frame)
    cv2.imwrite("Images/"+name+".jpg",frame)
    k = cv2.waitKey(1)
    
    if k == ord('q'):
       break
      
update_frame()
    


    
         

 
    


btn=tk.Button(win,text="Show & Save",command=update_frame,bg='yellow',fg='blue',font="sarif 18 bold")
btn.place(x=130,y=210)


cap.release()
 

 
win.mainloop()

