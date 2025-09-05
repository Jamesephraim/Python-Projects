import socket
import os
import cv2
import imutils
import numpy as np
import time
import base64

from tkinter import filedialog


camara=0
def receive_file():

    c=socket.socket()

    host=str(input('[+] Enter Server IP :'))
    #host='127.0.0.1'
    #port=1235
    port =int(input('[+] Enter port :'))

    c.connect((host,port))
    print('Connected')
    filename=str(input('[+] Enter You Want FilePath :'))
    c.send(bytes(filename,'utf-8'))
    #print(c.recv(1024).decode())
    #while True:
    data=c.recv(1024).decode()
    if not data:
        print("\n[-] No data in file\n")
    elif data:
        print('\n--> Received Data\n')
        n=input('[+] Which name to save File :')
        name='/home/ubentu/Desktop/My Project/FTP/'+n
        print(name)
        f=open(name,'w')
        f.write(str(data))
        f.close()
        print(data)

    c.close()
    return





def send_file():
        s=socket.socket()
        host=str(input('[+] Select You Ip :'))
        port=int(input('[+] Select Port Above (1024) :'))
        s.bind((host,port))
        s.listen(1)
        c,conn=s.accept()
        print(f'[++]Connected With Client {conn}')
        #receving File name
        filepath=c.recv(1024).decode()
        #file='empty.txt'
        print('[+] Requesting File -->',filepath)
        f=open(filepath,'r')
        data=f.read()
        
        
        while data:
                c.send((data).encode())
            
                
                data=f.read()
                if not data:
                    f.close()
                    print('[+] Sending Completed')
        s.close()
        return


def send_messenger():
    #You have Server
    key='exit'
    s=socket.socket()

    host=str(input("[+] Your Ip Address :"))
    port=int(input('[+] Select any port Above(1024) :'))
    name=input('[+] Enter Your name :')
    alert='\n'+name+' Disconnect You can Type [exit]'
    s.bind((host,port))
    s.listen(1)
    c,conn=s.accept()
    print(f'Connected with {conn}')
    c.send(bytes(name.encode()))
    another_name=c.recv(1024).decode()
    while True:
        msg=input(f'[+] {name} :')
        if msg==key:
            break
        c.send(bytes(msg,'utf-8'))
        another_msg=c.recv(1024).decode()
        print(f'[+] {another_name} : {another_msg}') 
         
    #c.send(bytes(alert,'utf-8'))
    c.close()
  
    return




def receive_messenger():
    #Client
    key='exit'
    c=socket.socket()
    host=str(input("[+] Server Ip Address :"))
    port=int(input('[+] Server Port :'))
    name=input('[+] Enter Your name :')
    alert='\n'+name+' Disconnect You can Type [exit]'
    c.connect((host,port))
    another_name=c.recv(1024).decode()
    c.send(bytes(name,'utf-8'))
    while True:
        print(f'[+] {another_name} :',c.recv(1024).decode())
        msg=input(f'[+] {name} :')
         
        c.send(bytes(msg,'utf-8'))
        if msg==key:
            break
         
    #c.send(bytes(alert,'utf-8'))
    c.close()


    


    return


def help():
    print(' ______________________________________')
    print('|______________--Help Menu--___________|\n\n\n')

    print('*'*40)
    print('|----------[1] Receive File -----------|')
    print('*'*40)

    print('[+] After Server Configration (or) After Sender Creating a FTP Server')
    print('[+] Enter Valid Server Ip ')
    print('[+] Enter Valid Server Port ')
    print('[+] Enter You Want Any Valid FilePath Stored in Server Computer')







    return


def send_image():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #IPV4,TCP
    #host='127.0.0.1'
    host=str(input('[+] Set Server IP :'))
    port=int(input('[+] Set Port :'))
    s.bind((host,port))
    s.listen(1)
    c,addr=s.accept()
    print(f'Connected With {addr}')
    path=str(input('+] Enter Path :'))
    #'/home/ubentu/Desktop/My Project/Images/1.jpeg'
    print(f'Sending {path}')
    file=open(path,'rb')
    image_data=file.read(2048)
    while image_data:
        c.send(image_data)
        image_data=file.read(2048)
    #file.write()


    file.close()
    s.close()

    return

def receive_image():
    c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #IPV4,TCP
    #host='127.0.0.1'
    #port=1234
    host=str(input('[+] Enter Server IP :'))
    port=int(input('[+] Enter Server Port :'))
    c.connect((host,port))
    
    f_name=input('[+] Which name You Want To Save :')
    save_path=f'/home/ubentu/Desktop/My Project/Socket Image/{f_name}'
    file=open(save_path,'wb')
    print('Receiving Image')
    image_data=c.recv(2048)

    while image_data:
        file.write(image_data)
        image_data=c.recv(2048)

    print(f'Received Image stored at {save_path}')
    file.close()
    c.close()
    return
    
def View_all_images():
    #--------------------Display All Files in the Folder--------------------
    #Display All files and Folders
    i,j,k,l=0,0,0,0
    path=filedialog.askdirectory(title='Open Folder')#filetypes=[('Text FIles','.txt'),('Python','.py'),('All Files','*.*')])
    #path='/home/ubentu/Desktop/My Project/'
    print(path)
    all_files=os.listdir(path)
    print('\n\n\n|----------- Images in Server ------------|\n')
    for file_names in all_files:
        if '.jpg' in  file_names:
            i+=1   
            print(f'[ + ] {path}{file_names}')
        elif '.jpeg' in  file_names:
            j+=1   
            print(f'[ + ] {path}{file_names}')
        elif '.png' in  file_names:
            k+=1   
            print(f'[ + ] {path}{file_names}')
        elif '.bng' in  file_names:
            l+=1   
            print(f'[ + ] {path}{file_names}')


    print(f'\n|------------ Total JPG Files {i} -----------|')
    print(f'|------------ Total JPEG Files {j} ----------|')
    print(f'|------------ Total PNG Files {k} -----------|')
    print(f'|------------ Total BNG Files {l} -----------|\n\n')
    #-----------------------------------------------------------------------1
    return


def send_cam():
    """ cap=cv2.VideoCapture(camara)
    BUFF=65536
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF)

    host=str(input('[+] Set Server Ip :'))
    while True:
        port=int(input('[+] Enter Server Port :'))
        if ( port > 65536):
            print('[-] Please Enter Valid Port Below(65536) ')
            
        elif ( port < 1024):
            print('[-] Please Enter Valid Port Above(1024)  ')

        else:
            break

    s.bind((host,port))
    #s.listen()
    print(host,port)
    print('[+] Listening for Incoming Connnections ...........')

    while True:
        WIDTH=400
        c,addr=s.recvfrom(BUFF)
        print(f'[+] Connected From {addr}')
        print('[+] Sending Your Camara..........')
        while (cap.isOpened()):
            _,frame=cap.read()
            frame=imutils.resize(frame,width=WIDTH)
            encode,buffer=cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
            message=base64.b64encode(buffer)
            s.sendto(message,addr)

            cv2.imshow('Sending Camara',frame)
            if cv2.waitKey(1) == ord('1'):
                s.close()
                break """

    cam=0
    BUFF=65536
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF)

    host_name=socket.gethostname()

    host_ip=str(input('Create a New Server IP :'))
    while True:
            port=int(input('[+] Enter Server Port :'))
            if ( port > 65536):
                print('[-] Please Enter Valid Port Below(65536) ')
                
            elif ( port < 1024):
                print('[-] Please Enter Valid Port Above(1024)  ')

            else:
                break
    print('Listening Incomming Connections.........')
    socket_address=(host_ip,port)
    server_socket.bind(socket_address)


    vid=cv2.VideoCapture(cam)
    fps,st,client_to_count,cnt=(0,0,20,0)

    while True:
        msg,client_addr=server_socket.recvfrom(BUFF)
        print("Connection From",client_addr)
        print('[+] Sending Your Video.........')
        WIDTH=400
        while(vid.isOpened()):
            _,frame=vid.read()
            frame=imutils.resize(frame,width=WIDTH)
            encoded,buffer=cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
            message=base64.b64encode(buffer)
            server_socket.sendto(message,client_addr)
            cv2.imshow("Transmiting Video",frame)
            key=cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                server_socket.close()
                break






    
    return



def receive_cam():


    """ BUFF=65536
    c=socket.socket()
    c.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF)

    host=str(input('[+] Enter Server Ip :'))
    while True:
        port=int(input('[+] Enter Server Port :'))
        if ( port > 65536):
            print('[-] Please Enter Valid Port Below(65536) ')
            
        elif ( port < 1024):
            print('[-] Please Enter Valid Port Above(1024)  ')

        else:
            break
        
    print(host,port)
    message=b"hello"

    c.sendto((host,port))

    while True:
        packet,_=c.recvfrom(BUFF)
        data=base64.b64decode(packet)
        npdata=np.fromstring(data,dtype=np.uint8)
        frame=cv2.imdecode(npdata,1)
        cv2.imshow('Receving Video..',frame)
        
        if cv2.waitKey(1) ==ord('q'):
            c.close()
            break



    return

 """
    

    BUFF=65536
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF)



    host_name=socket.gethostname()

    host_ip=str(input('Enter Server IP :'))
    while True:
            port=int(input('[+] Enter Server Port :'))
            if ( port > 65536):
                print('[-] Please Enter Valid Port Below(65536) ')
                
            elif ( port < 1024):
                print('[-] Please Enter Valid Port Above(1024)  ')

            else:
                break

    print(host_ip,port)
    message=b"hello"
    client_socket.sendto(message,(host_ip,port))

    while True:
        packet,_=client_socket.recvfrom(BUFF)
        data=base64.b64decode(packet)
        npdata=np.fromstring(data,dtype=np.uint8)
        frame=cv2.imdecode(npdata,1)
        cv2.imshow("Receving Video",frame)
        
        
        key=cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            
            client_socket.close()
            break
        




    

while True:
#-------------------------------------
    print('-'*60)
    print('[ 1 ] Receive File')
    print('[ 2 ] Send File')
    print('[ 3 ] View All Files')

    print('[ 4 ] Client Receive Messenger')
    print('[ 5 ] Server Send Messenger')

    print('[ 6 ] Send Image')
    print('[ 7 ] Receive Image')
    print('[ 8 ] View All Images')

    print('[ 9 ] Send Webcam')
    print('[10 ] Receive Webcam')

    print('[11 ] Send Video')
    print('[12 ] Receive Video')
    print('[13 ] View All Videos')

    print('[99 ] Help')
    print('[00 ] Exit')

    key=int(input('Enter Choice:'))

    #---------------files---------
    if key == 1:
        receive_file()
    elif key == 2:
        send_file()
    elif key == 3:
        pass

    #---------------messages------------
    
    elif key == 4:
        send_messenger()

    elif key == 5:
        receive_messenger()

    #-----------------Images-------------

    elif key == 6:
        send_image()
    elif key == 7:
        receive_image()
    elif key == 8:
        View_all_images()

    #-------------------------Webcamara-----------
    elif key == 9:
        send_cam()
    elif key == 10:
        receive_cam()
    

    elif key == 99:
        help()

    elif key == 00:
        exit()
    else:
        print('Invalid Input')
        





#setsockopt,recvfrom,cv2.imencode,base64.b64encode,
