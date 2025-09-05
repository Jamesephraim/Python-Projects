import cv2,socket
import imutils
import numpy as np
import time
import base64

#
#pip install imutils,sockets,opencv-python,numpy
#
#
#



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
     



