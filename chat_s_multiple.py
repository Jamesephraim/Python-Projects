import socket
import threading



def incoming_connection():
    while True:
        c,addr=s.accept()
        print(f'[+] Connected With {addr}')
        c.send(bytes('You Now Connected To Server','utf-8'))
        addresses[c]=addr
        threading.Thread(target=handle_client,args=(c,)).start()

def handle_client(c):
    name=c.recv(BUFF_LOW).decode('utf-8')
    wel=f'Welcome to {name}'
    c.send(bytes(wel,'utf-8'))
    msg=f'{name} Joined to Chat'
    broadcast(bytes(msg,'utf-8'))
    clients[c]=name

    while True:
        msg=c.recv(BUFF_HIGH)
        if msg != bytes('exit','utf-8'):
            broadcast(msg,name+':')
        
        else:
            c.send(bytes('quit','utf-8'))
            c.close()
            del clients[c]
            broadcast(bytes(f'{name} Has Now Left Chat !! '))
            break


def broadcast(msg,name=''):
    for x in clients:
        x.send(bytes(name,'utf-8')+msg)









ip=str(input('[+] Set Ip :'))
port=int(input('[+] Set Port :'))


addresses={}
clients={}
BUFF_LOW=1024
BUFF_HIGH=2048

s=socket.socket()
s.bind((ip,port))
print(ip,port)
if s:
    s.listen()
    print('[+] Waiting For Incoming Connections..........')
    t=threading.Thread(target=incoming_connection)
    t.start()
    t.join()
    s.close()