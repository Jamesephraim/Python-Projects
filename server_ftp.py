import socket

def server():

        s=socket.socket()

        host=str(input('Select You Ip :'))
        port=int(input('Select Port Above (1024) :'))

        s.bind((host,port))



    
        s.listen(1)
        c,conn=s.accept()
        print(f'Connected With Client {conn}')
        #receving File name
        filepath=c.recv(1024).decode()
        print('Requesting File -->',filepath)

        fo=open(filepath,'r')
        
        data=fo.read()
        
        
        
        while data:
                c.send(str(data).encode())
            
                data=fo.read()
                

                
                if not data:
                    fo.close()
                    print('Sending Completed')
        s.close()
        return
                
            
            

def client():
    c=socket.socket()
    host=str(input('Enter Server IP :'))
    #host='127.0.0.1'
    #port=1235
    port =int(input('Enter port :'))
    c.connect((host,port))
    print('Connected')
    filename=str(input('Enter You Want FilePath :'))
    #sending File name
    c.send(bytes(filename,'utf-8'))
    #print(c.recv(1024).decode())
    #while True:
    data=c.recv(1024).decode()
    if not data:
        print("\nNo data in file\n")

    elif data:
        print('\n--> Received Data\n')
        print(data)
    c.close()
    return



while True:
#-------------------------------------
    print('-'*60)
    print('[ 1 ] Receive File')
    print('[ 2 ] Send File')

    print('[ 3 ] Help')
    print('[ 4 ] Exit')

    key=int(input('Enter Choice:'))
    if key == 1:
        client()
    elif key == 2:
        server()

    elif key == 3:
        print('Help')

    elif key == 4:
        exit()
    else:
        print('Invalid Input')
        




