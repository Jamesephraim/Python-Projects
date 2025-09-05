
import socket



s=socket.socket()

#host=str(input('Create a New Server IP :'))
#host='127.0.0.1'
#port=1235
host=socket.gethostname()
print(host)
port =int(input('Select Any port Above (1024) :'))

print(host,':',port)

s.bind((host,port))

totalConnections=int(input('Enter How Many Clients :'))



s.listen(totalConnections)

clients=[]


print('Initiating Clients')

for i in range(totalConnections):
    conn=s.accept()
    clients.append(conn)
    print('Connected With Client',i+1)


fileno=0
index=0
for conn in clients:
    index=index+1
    data=conn[0].recv(1024).decode()
    if not data:
        continue
    filename='main_'+str(fileno)+'.txt'
    fileno=fileno+1


    fo=open(filename,'w')


    while data:
        if not data:
            continue
        else:
            fo.write(data)
            data=conn[0].recv(1024).decode()
    print("[+] Reciving File Client",index)
    print('[+] Received  Successfully ! New File Created',filename)
    fo.close()

for conn in clients:
    conn[0].close()



 