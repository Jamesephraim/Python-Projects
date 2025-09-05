import cv2 as cv

from tkinter import *


win=Tk()

win.geometry("500x300")
#win.resizable(False,False)

def show():
        cam=cv.VideoCapture(0)
        result, image=cam.read()
        label['text']=cv.imshow('Hello',image)
        
 

frame=Frame(win,highlightbackground='black',highlightthickness=1)

label=Label()
label.place(x=170)
frame.place(x=160)
frame.configure(height=200,width=200)

#label=Label(frame,text="H",bg='yellow',fg='blue',width=30)
#label.pack(pady=20)

#show camara
show=Button(text="Show Cam",bg="blue",fg='white',command=show)
show.place(x=160,y=220)
#Save camara
save=Button(text="Save",bg="red",fg='white')
save.place(x=260,y=220)




#cam=cv.VideoCapture(0)
#result, image=cam.read()
#if result:
	#cv.imshow('Hello',image)
	#cv.imwrite("mypic.png",image)
	#cv.waitkey(100)
	#cv.destroyWindow('Destroy')


win.mainloop()
