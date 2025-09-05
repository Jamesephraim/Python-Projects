import numpy
from tkinter import *
import tkinter.messagebox
from pygame import mixer
import cv2
import time



#---------------Installing Packages------------
#
#pip install opencv-python
#
#pip install pygame
#
#
#
#
#
#----------------------------------------------





root=Tk()

#Window Height And Width
root.geometry('400x500')

#Creating a Frame With Full Window
frame=Frame(root,relief=RIDGE,borderwidth=6)
frame.pack(fill=BOTH,expand=1)

#Window Title
root.title('WebServer')

#Frame background Setup
frame.config(background="orange")
heading_label=Label(frame,text="HD Camara",fg="white",bg="blue",font="Sarif 20 bold")
heading_label.pack(side=TOP,fill=X)


#bg_img=PhotoImage(file="C:\Users\lenovo\Desktop\Python\john.png")
#bg_label=Label(frame,image=bg_img)
#g_label.pack(side=TOP)



#
#------------------Capture Noraml Image Function--------------
#

def capture_normal_image():

    cam=cv2.VideoCapture(0)

    #if cam.isOpened():
        

    while True:
            ret,frame=cam.read()
             
             
            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)
            cv2.imshow("Capture Normal Color",frame)
            k=cv2.waitKey(1)
            if k == ord('q'):
                break
    cam.release()
    cv2.distroyAllWindows()

#
#------------------Capture Gray Image Function--------------
#


def capture_gray_image():

    cam=cv2.VideoCapture(0)

    #if cam.isOpened():
        

    while True:
            ret,frame=cam.read()
            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            
            cv2.imshow("Capture Gray Color",gray)
            k=cv2.waitKey(1)
            if k == ord('q'):
                break
    cam.release()
    cv2.distroyAllWindows()


def capture_edge_image():

    cam=cv2.VideoCapture(0)

    #if cam.isOpened():
        

    while True:
            ret,frame=cam.read()
            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            canny=cv2.Canny(gray,190,100)

            cv2.imshow("Capture Edges",canny)
            k=cv2.waitKey(1)
            if k == ord('q'):
                break
    cam.release()
    cv2.distroyAllWindows()

 

menu=Menu(root)

root.config(menu=menu)


sub_menu1=Menu(menu)
menu.add_cascade(label="Image Capture",menu=sub_menu1)
sub_menu1.add_command(label="Capture Normal Photo",command=capture_normal_image)
sub_menu1.add_command(label="Capture Gray Photo",command=capture_gray_image)
sub_menu1.add_command(label="Capture Edges Photo",command=capture_edge_image)
 



sub_menu2=Menu(menu)
menu.add_cascade(label="Video Capture",menu=sub_menu2)
sub_menu2.add_command(label="Capture Normal Video")
sub_menu2.add_command(label="Capture Gray Video")
sub_menu2.add_command(label="Capture Edges Video")
 


sub_menu3=Menu(menu)
menu.add_cascade(label="Help",menu=sub_menu3)
sub_menu3.add_command(label="Exit")
















root.mainloop()
