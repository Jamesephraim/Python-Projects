import socket
import os
import colorama

def receive():
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

def send():
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

def View_all_files():
    #--------------------Display All Files in the Folder--------------------
    #Display All files and Folders
    i,j,k,l=0,0,0,0
    path='/home/ubentu/Desktop/My Project/Socket Image/'
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


while True:
    
    print('\n\n\n-------------------------------------------')
    print('[ 1 ] Send Image')
    print('[ 2 ] Receive Image')
    print('[ 3 ] View All Files')
    
    print('[ 9 ] Exit')

    key=int(input('[ + ] Enter Value :'))
    if key == 1:
        send()
    elif key == 2:
        receive()
    elif key == 3:
        View_all_files()
    
    elif key == 9:
        exit()
    else:
        print('Invalid Input')