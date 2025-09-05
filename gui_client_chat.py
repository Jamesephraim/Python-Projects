""" import socket
import threaded as td
import tkinter as tk
from tkinter import simpledialog

HOST='127.0.0.1'
PORT=1234

class Client:
    def __init__(self,host,port):
        self.sock=socket.socket()
        self.sock.connect((host,port))

        msg=tk.Tk()
        msg.withdraw()

        self.name=simpledialog.askstring('UserName','Enter Your Name:',parent=msg)
        
        self.gui_done=False

        self.running=True

        gui_thread=td.Thread(target=self.gui_loop)
        receive_thread=td.Thread(target=self.receive) 
        
        gui_thread.start()
        receive_thread.start()


    def gui_loop(self):
        self.win=tk.Tk()
        self.win.geometry('500x400')

        self.label=tk.Label(self.win,text='Chat',bg='gray')
        self.label.config(font='Arial 13')
        self.label.pack(padx=20,pady=5)



        self.msg_label=tk.Label(self.win,text='Message',bg='skyblue')
        self.msg_label.config(font='Arial 13')
        self.msg_label.pack(padx=20,pady=5)


        self.input=tk.Text(self.win,height=1)
        self.input.pack(padx=20,pady=5)



        self.send=tk.Button(self.win,text='Send',command=write)
        self.send.pack(padx=20,pady=5)

        self.gui_done=True

        self.win.protocol("WM_DELETE_WINDOW",self.stop)
        self.win.mainloop()

    def write(self):
        message=f'{self.name} : {self.input.get('1.0','end')}'
        self.sock.send(message.encode('utf-8'))
        self.input.delete('1.0','end')

    def receive(self):
        while self.running:

            try:
                message=self.sock.recv(1024)
                if message == 'Hello':
                    self.sock.send(self.name.encode('utf-8'))

                else:
                    if self.gui_done:
                        self.msg_label.config(state='normal')
                        self.msg_label.insert('end',message)
                        self.msg_label.yview('end')
                        self.msg_label.config(state='disabled')

            except ConnectionAbortedError:
                break

            except:
                print('Error')
                self.sock.close()
                break

     

    def stop(self):
        self.running=False
        self.win.destroy()
        self.sock.close()
        exit(0)


client=Client(HOST,PORT)



threading """
















#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top,textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 3300
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution