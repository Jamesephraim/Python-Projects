import socket
import threading


name=''
def receive():
    
    while True:
        try:
            msg=c.recv(BUFF_LOW).decode('utf-8')
            
            name=str(input('[+] Enter You Name :'))
            c.send(bytes(name,'utf-8'))
            print(f'[+] {msg}')

        except:
            print('[-] An Error Occurred in Server  !! ')
            c.close()
            break

def write():
    #message=f'{name} : {input('')}'
    message=input(f'{name} : ')
    c.send(bytes(message,'utf-8'))




if True:
    ip=str(input('[+] Enter Server Ip :'))
    port=int(input('[+] Enter Sever Port :'))
    BUFF_LOW=1024
    BUFF_HIGH=2048
    c=socket.socket()
    c.connect((ip,port))
    r=threading.Thread(target=receive)
    r.start()
    w=threading.Thread(target=write)
    w.start()
