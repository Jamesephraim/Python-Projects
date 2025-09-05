



import socket
from threading import Thread

def incoming_connections():

    while True:
        client,addr=s.accept()
        print(f'{addr} Client is Connected ')
        client.send(bytes('You Now Connected','utf-8'))
        addresses[client]=addr
        Thread(target=handle_client,args=(client,)).start()

def handle_client(client):
    U_name=client.recv(BUFF).decode('utf-8')
    welcome=f"{ U_name} Welcome to Chat !"
    client.send(bytes(welcome,'utf-8'))
    msg=f'{U_name} Joined'
    broadcast(bytes(msg,'utf-8'))
    clients[client]=U_name

    while True:
        msg=client.recv(BUFF)
        if msg != bytes('{quit}','utf-8'):
            broadcast(msg,U_name+':')
        else:
            client.send(bytes('quit','utf-8'))
            client.close()
            del clients[client]
            broadcast(bytes(f'{U_name} has Left the Chat','utf-8'))
            break



def broadcast(msg,name=""):
    #send All connected clients broadcast message
    for x in clients:
        x.send(bytes(name,'utf-8')+msg)


clients={}
addresses={}

BUFF=1024
host=input('[+] Set Server Host :')
port=int(input('[+] Set Server Port :'))
print(host,port)
s=socket.socket()
s.bind((host,port))

if True:
    s.listen(5)
    print(host,port)
    print('Waiting For Incoming Connections.........')
    thread=Thread(target=incoming_connections)
    thread.start()
    thread.join()
    s.close()