import numpy
from tkinter import *
import tkinter.messagebox
from pygame import mixer
import cv2
import time
from PIL import Image, ImageTk
import tkinter as tk
import numpy as np



#---------------Installing Packages------------
#
#pip install opencv-python
#
#pip install pygame
#pip install tkintertable
#
#
#
#
#
#-----------------------------------------------




#camara='/home/ubentu/Videos/road4.mp4'
camara=0
root=Tk()

#Window Height And Width
root.geometry('700x500')

heading_label=tk.Label(root,text="HD Camara",fg="white",bg="blue",font="Sarif 20 bold")
heading_label.pack(side=TOP,fill=X)

#Creating a Frame With Full Window
frame=tk.Frame(root,relief=RIDGE,borderwidth=6)
frame.pack(fill=BOTH,expand=1)

#Window Title
root.title('WebServer')

#Frame background Setup
frame.config(background="orange")
 



#bg_img=PhotoImage(file="C:\Users\lenovo\Desktop\Python\john.png")
#bg_label=Label(frame,image=bg_img)
#g_label.pack(side=TOP)



 

 


 




#=====================================================#
#             Image Functions Starting                #
#=====================================================#





#
#------------------Capture Noraml Image Function--------------
#

def capture_normal_image():

    cam=cv2.VideoCapture(camara)

    #if cam.isOpened():
    #C:\Users\lenovo\Desktop\Python\Py-Projects\Camara Software   

    while True:
            ret,frame=cam.read()
             
            if ret:
                #print(ret)
                frame=cv2.resize(frame,(400,300))
                 
                
                
                font=cv2.FONT_ITALIC
                cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
                cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)
                 
                cv2.imshow("Capture Normal Color",frame)
                 
                k=cv2.waitKey(10)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="Normal_Image.png"
                cv2.imwrite(name,frame)
                #cv2.putText(frame,'Image Saved',(500,450),font,0.6,(255,0,0),2)
                 
                
    #capture_normal_image()          
    cam.release()
    cv2.destroyAllWindows()
#
#------------------Capture Gray Image Function--------------
#


def capture_gray_image():

    cam=cv2.VideoCapture(camara)

    #if cam.isOpened():
    #C:\Users\lenovo\Desktop\Python\Py-Projects\Camara Software   

    while True:
            ret,frame=cam.read()
            frame=cv2.resize(frame,(400,300))
            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            
            cv2.imshow("Capture Gray Color",gray)
            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="Gray_Image.png"
                cv2.imwrite(name,gray)
    cam.release()
    cv2.destroyAllWindows()


#------------RGB Format Images --------------

def capture_rgb_image():

    cam=cv2.VideoCapture(camara)

    #if cam.isOpened():
    #C:\Users\lenovo\Desktop\Python\Py-Projects\Camara Software   

    while True:
            ret,frame=cam.read()
            #frame=cv2.resize(frame,(400,300))
            frame=cv2.resize(frame,(400,300))
            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)
            img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            
            cv2.imshow("Capture RGB Color",img)
            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="RGB_Image.png"
                cv2.imwrite(name,img)
                
    cam.release()
    cv2.destroyAllWindows()


#------------Edges Captures Images --------------

def capture_edge_image():

    cam=cv2.VideoCapture(camara)

    #if cam.isOpened():
    #C:\Users\lenovo\Desktop\Python\Py-Projects\Camara Software    

    while True:
            ret,frame=cam.read()
            frame=cv2.resize(frame,(400,300))
            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            canny=cv2.Canny(gray,75,150)

            cv2.imshow("Capture Edges",canny)
            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="Edge_Image.png"
                cv2.imwrite(name,canny)
    cam.release()
    cv2.destroyAllWindows()


#------------Moving Area Images --------------



def capture_moving_area():
    
        cam=cv2.VideoCapture(camara)


        while cam.isOpened():
            ret,frame1=cam.read()
            ret,frame2=cam.read()

            diff=cv2.absdiff(frame1,frame2)
            font=cv2.FONT_ITALIC
            cv2.putText(frame1,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame1,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)


            gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

            _,thresh=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
            dilated=cv2.dilate(thresh,None,iterations=3)

            contours,_ =cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            for c in contours:
                if cv2.contourArea(c) <5000:
                    continue
                x,y,w,h=cv2.boundingRect(c)
                cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow("Motion Detection",frame1)

            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="Moving_Image.png"
                cv2.imwrite(name,frame1)

        cam.release()
        cv2.destroyAllWindows()

#------------Shadow Format Images --------------

def capture_shadow_area():
    print('Shadow Motion Detection')

    cam=cv2.VideoCapture(camara)

    #al1=cv2.createBackgroundSubtractorMOG2(detectShadows=True)
    al2=cv2.createBackgroundSubtractorKNN(detectShadows=True)

    while True:
        ret,frame=cam.read()
        frame=cv2.resize(frame,(400,300))
        font=cv2.FONT_ITALIC
        cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
        cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)

        #res1=al1.apply(frame)
        res2=al2.apply(frame)
        #50% Ok
        #cv2.imshow('Res1',res1)
        #80-90% Ok
        cv2.imshow('Shadow Motion Detection',res2)
        #print(res2)
        #Real Frame
        #cv2.imshow('Frame',frame)

        k=cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('s'):
                name="Shadow_Image.png"
                cv2.imwrite(name,res2)

    cam.release()
    cv2.destroyAllWindows()

 
#
#-----------------capture_thresh_binary_area----------------
#


def capture_thresh_binary_area():


    cam=cv2.VideoCapture(camara)

    while True:
            ret,frame=cam.read()
            frame=cv2.resize(frame,(400,300))
            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)

            _,th1=cv2.threshold(frame,127,255,cv2.THRESH_BINARY)

            cv2.imshow('THRESH_BINARY',th1)


            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="Binary_Thresh_Image.png"
                cv2.imwrite(name,th1)

    cam.release()
    cv2.destroyAllWindows()


#
#-----------------capture_adaptive_thresh_mean----------------
#

def capture_adaptive_thresh_mean():


    cam=cv2.VideoCapture(camara)

    while True:
            ret,frame=cam.read()
            frame=cv2.resize(frame,(400,300))

            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)

            #THRESH_BINARY
            _,th1=cv2.threshold(frame,127,255,cv2.THRESH_BINARY)

#----------------------NOT WORKING IN THIS FUNCTION----------------------#
            
            #ADAPTIVE_THRESH_MEAN_C
            #th2=cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,4)
            #ADAPTIVE_THRESH_GAUSSIAN_C
            #th3=cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
            #print(th2)
            #cv2.imshow('Normal',frame)
            
            #cv2.imshow('ADAPTIVE_THRESH_MEAN_C',th2)
            #cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C',th3)

#-----------------------------------------------------------------------#
            cv2.imshow('ADAPTIVE_THRESH_MEAN',th1)

            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="ADAPTIVE_THRESH_MEAN_Image.png"
                cv2.imwrite(name,th1)

    cam.release()
    cv2.destroyAllWindows()



#--------------------------------------


def capture_hsv_image():


    cam=cv2.VideoCapture(camara)

    while True:
            ret,frame=cam.read()
            frame=cv2.resize(frame,(400,300))
             


            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)

            hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            cv2.imshow('HSY',hsv_img)

            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="COLOR_BGR2HSV.png"
                cv2.imwrite(name,hsv_img)


    cam.release()
    cv2.destroyAllWindows()
            


#----------------------capture_sobelx-------------

def capture_sobelx():


    cam=cv2.VideoCapture(camara)

    while True:
            ret,frame=cam.read()
            frame=cv2.resize(frame,(400,300))


            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(0,255,255),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(0,255,255),2)

            sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)


            cv2.imshow("Sobelx",sobelx)
            
            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="Sobel_X.png"
                cv2.imwrite(name,sobelx)


    cam.release()
    cv2.destroyAllWindows()



#----------------------capture_sobely-------------

def capture_sobely():


    cam=cv2.VideoCapture(camara)

    while True:
            ret,frame=cam.read()
            frame=cv2.resize(frame,(400,300))

            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)
            
            sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)


            cv2.imshow("Sobely",sobely)
            
            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="Sobel_Y.png"
                cv2.imwrite(name,sobely)


    cam.release()
    cv2.destroyAllWindows()



#----------------------capture_laplacian-------------

def capture_laplacian():


    cam=cv2.VideoCapture(camara)

    while True:
            ret,frame=cam.read()
            frame=cv2.resize(frame,(400,300))

            font=cv2.FONT_ITALIC
            cv2.putText(frame,'[q] Exit',(20,60),font,0.6,(255,0,0),2)
            cv2.putText(frame,'[s] Save Image',(20,100),font,0.6,(255,0,0),2)
            
            laplacian=cv2.Laplacian(frame,cv2.CV_64F)


            cv2.imshow("Laplacian",laplacian)
            
            k=cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                name="Laplacian.png"
                cv2.imwrite(name,laplacian)


    cam.release
    cv2.destroyAllWindows()



#---------------detect_circles------------------


def detect_circles():
    cam=cv2.VideoCapture(camara)

     
    while True:
        ret,frame=cam.read()
        blur=cv2.blur(frame,(3,3))
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #circles=detect_circles(gray)
        circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,100)
        if circles is not None:
            circles=np.round(circles[0, :]).astype('int')
            for (x,y,r) in circles:
                cv2.circle(gray,(x,y),r,(255,0,0),3)
                cv2.rectangle(gray,(x-2,y-2),(x+2,y+2),(255,0,0),0)

                cv2.imshow('Frame',gray)
        #cv2.imshow('Gray',gray)
        #cv2.imshow('Blur',blur)



        k=cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('s'):
                name="Detect Circle.png"
                cv2.imwrite(name,gray)
    cam.release()
    cv2.destroyAllWindows()


#---------------Detect Lines-----------------

def detect_line():
     
    cam=cv2.VideoCapture(0)

    while True:

        ret,img=cam.read()
        img=cv2.GaussianBlur(img,(5,5),0)
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        lower_yellow=np.array([18,94,140])#Yellow
        up_yellow=np.array([48,255,255])
        mask=cv2.inRange(hsv,lower_yellow,up_yellow)
        edges=cv2.Canny(mask,75,150)

        lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=70)
        if lines is not None:
            for line in lines:
                x1,y1,x2,y2=line[0]
                cv2.line(img,(x1,y1),(x2,y2),(200,0,0),2)
                


        
        cv2.imshow('Image',img)
        #cv2.imshow('Mask',mask)

        cv2.imshow('Canny',edges) 
        



        k=cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('s'):
                name="Detect Lines.png"
                cv2.imwrite(name,img)


    cam.release()
    cv2.destroyAllWindows()


    

#------------All Format Images --------------

def all_format_images():
    cam=cv2.VideoCapture(camara)
    
    while True:
            ret,frame=cam.read()
             
            #Resize opening Window
            frame=cv2.resize(frame,(400,300))

            
            #------------Normal Image Dispaly
            cv2.imshow("Capture Normal Color",frame)

            
            #Convert Gray
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #-----------Gray Image Display
            cv2.imshow("Capture Gray Color",gray)
            

            #Convert RGB
            img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            #------------RGB Image Display
            cv2.imshow("Capture RGB Color",img)
              
            
            #Convert Canny like , Edges Detecting
            canny=cv2.Canny(gray,190,100)
            #-----------Canny Display
            cv2.imshow("Capture Edges",canny)

            #HSV
            hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            #-----------HSV Display
            cv2.imshow('HSY',hsv_img)
            
#----------------------NOT WORKING IN THIS FUNCTION----------------------#
            #Convert Shadow Image
            #al1=cv2.createBackgroundSubtractorMOG2(detectShadows=True)
            #al2=cv2.createBackgroundSubtractorKNN(detectShadows=True)
            #res1=al1.apply(frame)
            #res2=al2.apply(frame)
            #print(res2)
            #-------------Display Shadow Image
            #cv2.imshow('Shadow Motion Detection 1',res1)
            #cv2.imshow('Shadow Motion Detection 2',res2)
#------------------------------------------------------------------------#

            k=cv2.waitKey(1)
            if k == ord('q'):
                break

    cam.release()
    cv2.destroyAllWindows()


     
#=====================================================#
#               Image Functions Ending                #
#=====================================================#



#=====================================================#
#               Video Functions Starting              #
#=====================================================#





























#=====================================================#
#              Video Functions Ending                 #
#=====================================================#

#
#----------------------------------------------
#

def close():
    exit()
    



#
#----------------------------------------------
#




menu=Menu(root)

root.config(menu=menu)


sub_menu1=Menu(menu,tearoff=False)
menu.add_cascade(label="Image Capture",menu=sub_menu1)
sub_menu1.add_command(label="Camara",command=camara)
sub_menu1.add_command(label="Capture Normal Photo",command=capture_normal_image)
sub_menu1.add_command(label="Capture Gray Photo",command=capture_gray_image)
sub_menu1.add_command(label="Capture RGB Photo",command=capture_rgb_image)
sub_menu1.add_command(label="Capture Edges Photo",command=capture_edge_image)
sub_menu1.add_command(label="Capture Moving Places",command=capture_moving_area)
sub_menu1.add_command(label="Capture Shadow Places",command=capture_shadow_area)
sub_menu1.add_command(label="Capture HSV Places",command=capture_hsv_image)
sub_menu1.add_command(label="Capture THRESH BINARY",command=capture_thresh_binary_area)
sub_menu1.add_command(label="Capture LAPLACIAN ",command=capture_laplacian)
sub_menu1.add_command(label="Capture SobelX ",command=capture_sobelx)
sub_menu1.add_command(label="Capture SobelY ",command=capture_sobely)
sub_menu1.add_command(label="Detect Circles",command=detect_circles)
sub_menu1.add_command(label="Detect Line",command=detect_line)


sub_menu1.add_command(label="ADAPTIVE THRESH MEAN",command=capture_adaptive_thresh_mean)
sub_menu1.add_command(label="Show All Formats",command=all_format_images)
 



sub_menu2=Menu(menu,tearoff=False)
menu.add_cascade(label="Video Capture",menu=sub_menu2)
sub_menu2.add_command(label="Capture Normal Video")
sub_menu2.add_command(label="Capture Gray Video")
sub_menu2.add_command(label="Capture Edges Video")
 


sub_menu3=Menu(menu,tearoff=False)
menu.add_cascade(label="Help",menu=sub_menu3)
sub_menu3.add_command(label="Exit",command=close)
















root.mainloop()
