import tkinter as tk
import socket 
from threading import Thread

my_m=''
my_mm=''

def receive():
    
    while True:
        try:
            msg=c.recv(BUFF).decode('utf-8')
            if msg == my_m:
                
                msg_list.insert(tk.END,msg)

            else:
                msg_list.insert(tk.END,msg)

        except OSError:
            pass

def send():
    mess=msg.get()
    my_m=mess
    msg.set("")
    c.send(bytes(mess,'utf-8'))
    if mess== '{quit}':
        c.close()
        root.destroy()


def help():
    win=tk.Toplevel()
    win.geometry('600x300')
    win.title('-- Help Window --')
    win.resizable(False,False)

    tk.Label(win,text="Help Window",font='Arial 16',bg='orange',fg='blue').pack(fill=tk.X)

    title=tk.Label(win,text="{quit} --> Exit Chat",font='Arial 16',bg='red',fg='blue',justify='left')
    title.pack(fill=tk.X)
    
    tk.Label(win,text="[+] First You Can Connect Server",font='Arial 16',bg='orange',fg='blue',justify='left').pack(fill=tk.X)
    tk.Label(win,text="[+] After Connect First You Enter Name in Input Box",font='Arial 16',bg='orange',fg='blue',justify='left').pack(fill=tk.X)


    win.mainloop()



root=tk.Tk()
root.title('Group Chatting')
root.geometry('420x550')
root.resizable(False,False)
msg=tk.StringVar()
msg.set("Enter Name")
frame=tk.Frame(root)
sb=tk.Scrollbar(frame)
msg_list=tk.Listbox(frame,height=25,width=50,yscrollcommand=sb.set)
msg_list.pack(side=tk.LEFT,fill=tk.BOTH)
msg_list.pack()
sb.pack(side=tk.RIGHT,fill=tk.Y)
sb.pack()

frame.pack()

entry=tk.Entry(root,width=25,font='Sarif 17 ',fg='blue',textvariable=msg)
entry.bind("<Return>",send)
entry.place(x=5,y=505)
send_btn=tk.Button(root,text='SEND',bg='red',font='Sarif 13 ',fg='blue',command=send)
send_btn.place(x=340,y=505)


menu=tk.Menu(root)
root.config(menu=menu)


sub_menu=tk.Menu(menu,tearoff=False)

menu.add_cascade(label='Help',menu=sub_menu)
sub_menu.add_command(label='Help',command=help)





host=input('[+] Enter Server Host :')
port=int(input('[+] Enter Server Port :'))

BUFF=1024
c=socket.socket()
c.connect((host,port))

receive_thread=Thread(target=receive)
receive_thread.start()

root.mainloop()






