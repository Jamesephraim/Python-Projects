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




