from tkinter import *
from PIL import ImageTk

window=Tk()

window.geometry("550x370")

window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLable=Label(window,image=backgroundImage)

bgLable.place(x=0,y=0)

#Creating a Title
#title=Label(window,title='Login Here')

def login():
    uname=user.get()
    upass=password.get()
    print(uname)
    print(upass)
    print('Clicked Login Button')


#Creating a frame like html 'div'
loginframe=Frame(window ,bg='red')#'-alpha',0.5
#Place Frame in window
loginframe.place(x=140,y=100)


#Form ki Icon
logo=PhotoImage(file='stu.png')
logoLabel=Label(loginframe,image=logo )
logoLabel.grid(row=0,column=0,columnspan=2)

#User LAbel
user=Label(loginframe,text='Username :',fg="blue",font=('Arial',12,'bold'))
user.grid(row=1,column=0)
#User Input Box
user=Entry(loginframe,fg="blue",font=('Arial',12))
user.grid(row=1,column=1)

#Password LAbel
password=Label(loginframe,text='Password :',fg="blue",font=('Arial',12,'bold'))
password.grid(row=2,column=0)
#Password Input Box
password=Entry(loginframe,fg="blue",font=('Arial',12))
password.grid(row=2,column=1)



#Button
login=Button(loginframe,command=login,text='Login',fg="blue",bg='red',font=('Arial',12,'bold'))
login.grid(row=5,column=1)



window.mainloop()
