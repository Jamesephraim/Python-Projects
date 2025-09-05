import cv2
import numpy as np


cap=cv2.VideoCapture('/home/ubentu/Videos/road4.mp4')

while True:
    ret,frame=cap.read()
    blur=cv2.blur(frame,(3,3))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #circles=detect_circles(gray)
    circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,100)
    if circles is not None:
        circles=np.round(circles[0, :]).astype('int')
        for (x,y,r) in circles:
            cv2.circle(gray,(x,y),r,(255,0,0),3)
            cv2.rectangle(gray,(x-5,y-5),(x+5,y+5),(0,0,255),-1)

            cv2.imshow('Frame',gray)
    #cv2.imshow('Gray',gray)
    #cv2.imshow('Blur',blur)



    k=cv2.waitKey(1)
    if k == ord('q'):
        break

