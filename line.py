import cv2
import numpy as np

#  /home/ubentu/Desktop/My Project/Images/4.jpeg
cap=cv2.VideoCapture('/home/ubentu/Videos/road7.mp4')

while True:

    ret,img=cap.read()
    img=cv2.resize(img,(400,350))

    #         [y1:y2,x1:x2]
    #   |
    #   |y2
    #   |
    #   |
    #   | y1
    #   |___x1_____x2____________



    if not ret:
        #print('No Frame')
        cap=cv2.VideoCapture('/home/ubentu/Videos/road7.mp4')
        #video=cv2.VideoCapture(0)
        continue

    #roi=img[100:700,400:1000]

    #-------------Driver Vision------------
            #top:down,left:right
    #droi=img[100:650,700:900]

    #---------------------------------
    #img=cv2.GaussianBlur(img,(5,5),0)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #lower_white=10,0,0
    #upper_white=182,17,85
    lower_yellow=np.array([0,0,230])#Yellow48,255,255 ----- # White and yellow 0,0,255:255,255,255
    up_yellow=np.array([255,255,255])
    mask=cv2.inRange(hsv,lower_yellow,up_yellow)
    edges=cv2.Canny(mask,200,250)

    lines=cv2.HoughLinesP(edges,2,np.pi/180,100,maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(img,(x1,y1),(x2,y2),(0,0,200),2)
            


    
    cv2.imshow('Image',img)
    #cv2.imshow('ROI',roi)
    #cv2.imshow('DROI',droi)


    cv2.imshow('Canny',edges) 
     



    k=cv2.waitKey(25)
    if k == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()