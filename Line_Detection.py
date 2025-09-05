import cv2
import numpy as np


cap=cv2.VideoCapture('/home/ubentu/Videos/road7.mp4')
#cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(500,400))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(gray,400,300)

    #HoughLinesP(frame,rho,theta,threshold,minlength,maxlength)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength=100,maxLineGap=10)

    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,200,200),2)

    cv2.imshow('Frame',frame)
    #cv2.imshow('Gray',gray)
    cv2.imshow('Edges',edges)

    if cv2.waitKey(1) == ord('q'):
        break
