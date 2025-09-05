import cv2
import numpy as np



cap=cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter("hello.mp4", fourcc, 5.0, (720,480))

 
while True:
    
    ret,frame=cap.read()


    image = cv2.resize(frame, (200,200))
    out.write(frame)
    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(40) == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()   
out.release()