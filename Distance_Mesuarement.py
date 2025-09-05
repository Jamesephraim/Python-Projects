import cv2
import cvzone
import threading
import time

from cvzone.FaceMeshModule import FaceMeshDetector

cap=cv2.VideoCapture(0)
c=1
detector=FaceMeshDetector(maxFaces=1)

def face_detect():

    while True:
        ret,img=cap.read()
        img,faces=detector.findFaceMesh(img,draw=True)
        

        if faces:
            face=faces[0]
            L=face[144]
            R=face[374]
            #cv2.line(img,L,R,(0,255,0),2)
            #cv2.circle(img,L,5,(255,0,0),cv2.FILLED)
            #cv2.circle(img,R,5,(255,0,0),cv2.FILLED)
            w,_=detector.findDistance(L,R)
            

            #finding the Focal Length
            W=3.3   #Width in CM's
            #d=50    #Distance B/W camara and Face Just Assume
            #f=(w*d)/W
            #print(f)
            f=840
            d=(W*f)/w

            
            #cv2.putText(img,f'Distance : {int(d)} cm',(face[10][0],face[10][1]),scale=2)---------Not Work in this case
            cvzone.putTextRect(img,f'Distance : {int(d)} cm',(face[100][0],face[10][1]),scale=2,border=2,offset=10)


        cv2.imshow('Frame',img)


        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    face_detect()
