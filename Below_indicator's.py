from tkinter import *
import tkinter as tk

root=tk.Tk()

root.geometry("500x300")
root.title("Indicator's")

#frame 1 Top


def switch(indicator,page):

    for h in options_fm.winfo_children():
       if isinstance(h, tk.Label):
            h['bg']='red'
            
    indicator["bg"]="yellow"

    for fm in main_fm.winfo_children():
        fm.destory()
    root.update()
    page()
    

top_frame=tk.Frame(root,height=48,bg="#960C96")

#Button Home
home=tk.Button(top_frame,text="HOME",bg="blue",fg='white',width=9,command=lambda:switch(indicator=home_indicator,page=home))
home.place(x=10,y=10)

#Home indicator
home_indicator=tk.Label(top_frame,height=10,width=9,bg="yellow")
home_indicator.place(x=10,y=40,height=3)

#Add button
add=tk.Button(top_frame,text="Add",bg="blue",fg='white',width=9,command=lambda:switch(indicator=add_indicator,page=add))
add.place(x=85,y=10)

add_indicator=tk.Label(top_frame,height=10,width=9)
add_indicator.place(x=86,y=40,height=3)

#Edit Button
edit=tk.Button(top_frame,text="Edit",bg="blue",fg='white',width=9,command=lambda:switch(indicator=edit_indicator,page=edit))
edit.place(x=160,y=10)


edit_indicator=tk.Label(top_frame,height=10,width=9)
edit_indicator.place(x=162,y=40,height=3)

#About Button
about=tk.Button(top_frame,text="About",bg="blue",fg='white',width=9,command=lambda:switch(indicator=about_indicator,page=about))
about.place(x=235,y=10)

about_indicator=tk.Label(top_frame,height=10,width=9)
about_indicator.place(x=236,y=40,height=3)

top_frame.pack(fill=X,side="top")




def home():

    home=tk.Frame(main_frame,bg="gray")

    home_label=tk.Label(home,text="Home Page 1")
    home_label.pack()
    home.pack(fill=tk.BOTH,expand=True)

def add():

    add=tk.Frame(main_frame,bg="green")

    add_label=tk.Label(add,text="Add Page")
    add_label.pack()
    add.pack(fill=tk.BOTH,expand=True)


def edit():

    edit=tk.Frame(main_frame,bg="green")

    edit_label=tk.Label(edit,text="Edit Page")
    edit_label.pack()
    edit.pack(fill=tk.BOTH,expand=True)


def about():

    about=tk.Frame(main_frame,bg="green")

    about_label=tk.Label(about,text="About Page")
    about_label.pack()
    about.pack(fill=tk.BOTH,expand=True)
    
#Main Frame
main_frame=tk.Frame(root)

home()
  
main_frame.pack(fill=tk.BOTH,expand=True)




 

root.mainloop()
