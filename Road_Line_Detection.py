import cv2
import numpy as np
import matplotlib as plt



video=cv2.VideoCapture('/home/ubentu/Videos/road7.mp4')#4,7
#video=cv2.VideoCapture(0)
print(video.isOpened())

while True:
    ret,frame=video.read()
    if not ret:
      
        video=cv2.VideoCapture('/home/ubentu/Videos/road7.mp4')
        
        continue

    frame=cv2.resize(frame,(600,450))
    frame=cv2.GaussianBlur(frame,(5,5),0)
         

    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_y=np.array([10,110,150])
    upper_y=np.array([88,200,255])
    mask=cv2.inRange(hsv,lower_y,upper_y)
    edges=cv2.Canny(mask,74,150)

    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=10)
    #print(lines)
    for line in lines:
        if lines is not None:
         
            x1,y1,x2,y2=line[0]
            
            cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),2)
            #cv2.addWeighted(frame, 1.0, frame, 1.0, 0.0)
    cv2.imshow('Image',frame)
    cv2.imshow('Edges',edges)
    #cv2.imshow('Mask',mask)


    key=cv2.waitKey(50)
    if key == ord('q') :
        break
         

         