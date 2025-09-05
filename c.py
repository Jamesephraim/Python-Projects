
import socket



c=socket.socket()

c.connect(('127.0.0.1',9977))
name=input("Enter Your Name :")
c.send(bytes(name,'utf-8'))
another_user=c.recv(1024).decode()

while True:
    send_data=input(f'[+] {name} :')
    c.send(bytes(send_data,'utf-8'))
    #return_data=c.recv(1024).docode()
    print(f"[-] {another_user}:", c.recv(1024).decode())
