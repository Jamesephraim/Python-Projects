import socket




#ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

s=socket.socket()


     

#host=str(input('Enter Server IP :'))
#host='127.0.0.1'
#port=1235
host=socket.gethostname()

 

port =int(input('Enter port :'))

s.connect((host,port))
print(host,port)
print('Connected')

# Transfer File
while True:
    print('[ 1 ] Send File')
    print('[ 3 ] Exit ')
    key=int(input('Enter Choice:'))


    if  key == 1:
        
            filename=str(input('Enter File Name :'))
            print(filename)
            fi=open(filename,'r')

                
            data=fi.read()
                #If data is yes or no
            if not data:
                print('[-] Empty File No Data in File')
                break

            while data:
                s.send(str(data).encode())
                data=fi.read()
                fi.close()

        

    elif key == 3:
        exit()
