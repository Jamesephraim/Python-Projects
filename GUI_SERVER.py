import tkinter as tk
#from tkinter import ttk
import socket

root=tk.Tk()

root.geometry('370x400')
root.resizable(False,False)
root.title('Server ')


s=socket.socket()

#Binding Server Data like 'Ip' and 'Port'
s.bind(('localhost',9999))

#Listening How many Clients
s.listen(3)


frame=tk.Frame(root,bg="blue")
frame.pack()

mess=tk.Label(frame).pack()

def data():
    
    msg=tk.Entry(width=20,font="Sarif 20 bold")
    msg.place(x=2,y=360)
    send=tk.Button(text="Send",bg="blue",fg='white',font="Sarif 13 bold")
    send.place(x=310,y=360)
    display_msg(msg)




def display_msg(msg):
    print(msg)
    mess["text"]=msg
    
    
    




 


 




root.mainloop()
data()