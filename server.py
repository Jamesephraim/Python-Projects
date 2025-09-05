import socket
 

s=socket.socket()
#print("[+] Socket Created Successfully")
host=socket.gethostname()
ip=socket.gethostbyname(host)

#host= input('[+] Set Host:')
port= int(input('[+] Set Port:'))


s.bind((ip,port))
print("\n\n-------------------------")
print("[+] Username :",host)
print("[+] IP :",ip)
print("[+] PORT :",port)
s.listen(2)

myname=input('[+] Enter Yor Name :')


print(f'\n\n[+] Waiting For Connections.... {ip,port}')
c,addr=s.accept()
name=c.recv(1024).decode()
print('[+] Connected With',addr,name)
c.send(bytes(myname,"utf-8"))
while True:
     
     
    print(f'[+] {name} :',c.recv(1024).decode())
     
    msg=input(f"[+] {myname} :")
    
    c.send(bytes(msg,"utf-8"))
     


c.close()
