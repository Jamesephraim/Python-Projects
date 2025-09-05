from tkinter import *
 
from PIL import Image,ImageFilter,ImageEnhance,ImageTk
from tkinter import filedialog 
import ttk
import os
import cv2
#from numpy as np
boss_icon='/home/ubentu/Desktop/boss.jpg'

width=1100
i=1100
height=750
j=750
global img
global outputimage



#oooooooooooooooooooooooooooooooooooooooooooooooooooooooo
##
#Emboss
#BLUR
# 
# 
# 
# 
# 
#
#



#ooooooooooooooooooooooooooooooooooooooooooooooooooooooo


##===============================================================
#                   FUNCTONS in Python File
##================================================================

# ----------------> Display Image
def display_image(img):
    disimage=ImageTk.PhotoImage(img)
    panel.configure(image=disimage)
    panel.image=disimage



#--------------------> Change Image

def change_image():
    global img
    filepath=filedialog.askopenfilename(title='Open Image')
    if filepath:
        img=Image.open(filepath)
        img=img.resize((width,height))
        display_image(img)


#---------------------> Save Image

def save_image():
    global img
    filepath=filedialog.asksaveasfile(defaultextension='.jpg')
    outputimage.save(filepath)



#------------------>CONTOUR

def contour():
    global img
    img=img.filter(ImageFilter.CONTOUR)
    display_image(img)


#------------------>DETAIL

def detail():
    global img
    img=img.filter(ImageFilter.DETAIL)
    display_image(img)


#------------------>EDGE_Enhance

def edge_enhance():
    global img
    img=img.filter(ImageFilter.EDGE_ENHANCE)
    display_image(img)


#------------------>Edge_enhance_more

def eem():
    global img
    img=img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    display_image(img)


#-------------------->Find Edges


def find_edge():
    global img
    img=img.filter(ImageFilter.FIND_EDGES)
    display_image(img)


#-------------------->SHARPEN


def sharpen():
    global img
    img=img.filter(ImageFilter.SHARPEN)
    display_image(img)

#-------------------->SMOOTH

def smooth():
    global img
    img=img.filter(ImageFilter.SMOOTH)
    display_image(img)

#-------------------->SMOOTH _MORE


def smooth_more():
    global img
    img=img.filter(ImageFilter.SMOOTH_MORE)
    display_image(img)


#-------------------->Find color 3d


def color3d():
    global img
    img=img.filter(ImageFilter.Color3DLUT)
    display_image(img)



#-------------------->Flip Image


def flip():
    global img
    img=img.transpose((Image.FLIP_LEFT_RIGHT))
    display_image(img)



#--------------------> ROTATE IMAGE


def rotate():
    global img
    img=img.rotate(90)
    img=img.resize((width,height))
    display_image(img)









#-------------------->Find Emboss


def emboss():
    global img
    img=img.filter(ImageFilter.EMBOSS)
    display_image(img)


#-------------------->Find Edges


def blur():
    global img
    img=img.filter(ImageFilter.BLUR)
    display_image(img)


#---------------> Glassiun Blur

def gblur():
    global img
    img=img.filter(ImageFilter.GaussianBlur)
    display_image(img)



def resize():
    global img
    global i,j
    #if i<=width & j<=height:
    img=img.resize((i,j))

    i=i-5
    j=j-5
    display_image(img)


def back():
    global img
    global i,j
    
    img=img.resize((i,j))

    i=i+5
    j=j+5
    #if i>=width & j>=height:
        

    display_image(img)


def brightness(brightness_pos):
    brightness_pos = float(brightness_pos)
    #print(brightness_pos)
    global outputimage
    enhancer = ImageEnhance.Brightness(img)
    outputimage = enhancer.enhance(brightness_pos)
    display_image(outputimage)



def sharpness(pos):
    global outputimage,img
    pos=float(pos)
    enhancer=ImageEnhance.Sharpness(img)

    outputimage=enhancer.enhance(pos)
    display_image(outputimage)


def contrast(pos):
    global outputimage,img

    pos=float(pos)
    enhancer=ImageEnhance.Contrast(img)
    outputimage=enhancer.enhance(pos)
    display_image(outputimage)


def color(pos):
    global outputimage,img

    pos=float(pos)
    enchancer=ImageEnhance.Color(img)
    outputimage=enchancer.enhance(pos)
    display_image(outputimage)


















##===============================================================
#                   FUNCTONS Ending in Python File
##================================================================









root=Tk()

screen_width=root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#mains.geometry("1000x700")
root.geometry(f"{screen_width}x{screen_height}")
root.title('Image Editor ')
#root.resizable(False,False)

img=Image.open("/home/ubentu/Desktop/My Project/Camara/boss.jpg")
#img=Image.new('RGB',(width,height),(90,0,50))
img=img.resize((width,height))
 

frame=Frame(root,bg='skyblue',width=screen_width,height=80)
frame.place(x=0,y=0)



#-------------------------Display Image on the Panel-----------------
panel=Label(root,width=width,height=height)
panel.place(x=270,y=80)
display_image(img)


heading=Label(frame,text="Image Editor",bg='orange',fg='blue',width=40,font='impact 30').place(x=350,y=3)

x=20

font_size=15
btn_width=20
btn_height=1

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='CONTOUR',bg='blue',fg='white',command=contour)
btn1.place(x=x,y=80)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='DETAIL',bg='blue',fg='white',command=detail)
btn1.place(x=x,y=120)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='EDGE_ENHANCE',bg='blue',fg='white',command=edge_enhance)
btn1.place(x=x,y=160)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='EDGE_ENHANCE_MORE',bg='blue',fg='white',command=eem)
btn1.place(x=x,y=200)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='FIND_EDGES',bg='blue',fg='white',command=find_edge)
btn1.place(x=x,y=240)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='SHARPEN',bg='blue',fg='white',command=sharpen)
btn1.place(x=x,y=280)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='SMOOTH',bg='blue',fg='white',command=smooth)
btn1.place(x=x,y=320)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='SMOOTH_MORE',bg='blue',fg='white',command=smooth_more)
btn1.place(x=x,y=360)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='Color3DLUT',bg='blue',fg='white',command="")
btn1.place(x=x,y=400)


btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='Flip',bg='blue',fg='white',command=flip)
btn1.place(x=x,y=440)


btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='Rotate',bg='blue',fg='white',command=rotate)
btn1.place(x=x,y=480)

btn1=Button(root,width=9,font=f'sarif {font_size}',text='Resize',bg='blue',fg='white',command=resize)
btn1.place(x=x,y=520)

btn1=Button(root,width=9,font=f'sarif {font_size}',text='ReBack',bg='blue',fg='white',command=back)
btn1.place(x=140,y=520)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='Emboss',bg='blue',fg='white',command=emboss)
btn1.place(x=x,y=600)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='BLUR',bg='blue',fg='white',command=blur)
btn1.place(x=x,y=640)

btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='GaussianBlur',bg='blue',fg='white',command=gblur)
btn1.place(x=x,y=680)


btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='Change Image',bg='blue',fg='white',command=change_image)
btn1.place(x=x,y=720)


btn1=Button(root,width=btn_width,font=f'sarif {font_size}',text='Save',bg='red',fg='white',command=save_image)
btn1.place(x=x,y=760)



#00000000000000000000000----------- Sliders -------------0000000000000000000000000


sliderframe=Frame(root,width=500,height=600,bg='green')
sliderframe.place(x=1400,y=80)


scale_x=1430

Brightness=Scale(root,label="Brightness",from_=0,to=4,orient=HORIZONTAL,length=360,font='arial 18',bg='red',resolution=0.1,command=brightness)
Brightness.set(1)
Brightness.place(x=scale_x,y=100)

Sharpness=Scale(root,label="Sharpness",from_=0,to=4,orient=HORIZONTAL,length=360,font='arial 18',bg='blue',resolution=0.1,command=sharpness)
Sharpness.set(1)
Sharpness.place(x=scale_x,y=200)


Contrast=Scale(root,label="Contrast",from_=0,to=4,orient=HORIZONTAL,length=360,font='arial 18',bg='orange',resolution=0.1,command=contrast)
Contrast.set(1)
Contrast.place(x=scale_x,y=300)


Color=Scale(root,label="Color",from_=0,to=4,orient=HORIZONTAL,length=360,font='arial 18',bg='green',resolution=0.1,command=color)
Color.set(1)
Color.place(x=scale_x,y=400)
















#0000000000000000000000000000000000000000000000000000000000000000000000000000000000

 



 











 


#**************************************************************************


menu=Menu(root)
root.config(menu=menu)
m1=Menu(menu,tearoff=False)
menu.add_cascade(label='Open',menu=m1)
m1.add_command(label='Open Image',command=change_image)
m1.add_command(label='Save Image',command=save_image)
m1.add_command(label='Exit')


root.mainloop()