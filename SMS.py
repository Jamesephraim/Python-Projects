import tkinter
from tkinter import *
#import tkinter as tk
win=Tk()
win.title("Student DataBase Management System")
win.geometry("1200x600")
#win.resizable(False,False)


###     Function's Starting


 
   
   










#Function's Ending



# top nav bar
nav=Frame(win,bg="blue",relief=GROOVE,borderwidth=9)
nav.pack(side="top")
nav_label=Label(nav,text="Welcome to User",padx=580,bg="white",fg="blue",font="Sarif 14 bold")
nav_label.pack(fill=Y,side="bottom")

#left side menu

frame1=Frame(win,bg="red",borderwidth=9)#,relief=GROOVE
#RAISED= right,bottom border
#sunken= left,top border
#GROOVER=4 sides border multi layer
frame1.pack(side="left",fill=Y)
#frame1.place(x=10,y=10)

 

#Frame 1
label_name=Label(frame1,text="MENU",bg="red",fg="yellow" ,font="Sarif 20 bold").pack(pady=20)
btn1=Button(frame1,text="HOME" ,bg="blue",width=9,height=2,fg="white",borderwidth=0,font="Arial 16 bold")
btn1.pack(padx=10)

btn2=Button(frame1,text="ADD",bg="blue",fg="white",width=9,height=2,borderwidth=0,font="Arial 16 bold")
btn2.pack(padx=10)

btn3=Button(frame1,text="EDIT",bg="blue",fg="white",width=9,height=2,borderwidth=0,font="Arial 16 bold")
btn3.pack(padx=10)

btn4=Button(frame1,text="DELETE",bg="blue",fg="white",width=9,height=2,borderwidth=0,font="Arial 16 bold")
btn4.pack(padx=10)

btn5=Button(frame1,text="SEARCH",bg="blue",fg="white",width=9,height=2,borderwidth=0,font="Arial 16 bold")
btn5.pack(padx=10)

btn6=Button(frame1,text="DISPLAY",bg="blue",fg="white",width=9,height=2,borderwidth=0,font="Arial 16 bold")
btn6.pack(padx=10)

#Frame 2

#btn7=Button(frame2,text="Button 7" ,bg="red",width=9,height=2,fg="blue",borderwidth=0,font="Arial 16 bold")
#btn7.pack(padx=10)

#btn8=Button(frame2,text="Button 8",bg="red",fg="blue",width=9,height=2,borderwidth=0,font="Arial 16 bold")
#btn8.pack(padx=10)

# Main Frame

main_frame=Frame(win,highlightbackground='white',highlightthickness=2,bg='skyblue')
main_frame.pack()
main_frame.configure(height=800,width=1110)


win.mainloop()






 




