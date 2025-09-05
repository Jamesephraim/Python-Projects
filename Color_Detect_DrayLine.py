import cv2
import numpy as np

cap=cv2.VideoCapture(0)
x_medium=y_medium=0
while True:
    ret,frame=cap.read()
    #print(frame.shape)
    #frame=cv2.resize(frame,(500,300))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Red Color
    low=np.array([0,99,175])
    high=np.array([255,255,255])
    mask=cv2.inRange(hsv,low,high)

    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #Find maximun Colored Area
    contours=sorted(contours,key=lambda x :cv2.contourArea(x),reverse=True)
    for cnt in contours:
        (x,y,w,h)=cv2.boundingRect(cnt)
        #Draw Rectangle
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        x_medium=int((x + x + w)/2)
        
         
         
        cv2.line(frame,(x_medium,0),(x_medium,480),(255,0,0),2)
        break
    
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask)



    if cv2.waitKey(1) ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()