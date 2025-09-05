from tkinter import *


def valid():
    val1=gender1.cget()
    print(val1)

root=Tk()
root.title('Chech Box')
root.geometry('500x200')
gender1=Checkbutton(root,text="Male")
gender1.place(x=10,y=30)
gender1=Checkbutton(root,text="Female")
gender1.place(x=100,y=30)



btn=Button(root,command=valid,text='Button')
btn.place(x=30,y=60)

root.mainloop()
