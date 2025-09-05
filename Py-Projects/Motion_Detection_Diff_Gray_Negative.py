import cv2
#Camara Opening
cam=cv2.VideoCapture(0)
#Print Camara Status
print(cam.isOpened())

#Capture Multiple Frames
while cam.isOpened():

    #Capture Frames 1
    ret, frame1=cam.read()

    #Capture Frames 2
    ret, frame2=cam.read()

    #Capture Difference Between Frames1 & Frame2
    diff=cv2.absdiff(frame1,frame2)

    #Convert Normal Image Frame To Gray Color
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    #Showing The Captured All Frames
    cv2.imshow('WebCam',gray)
    #Inturept if Press 'q' Stop The Captureing Frame into Webcam
    if cv2.waitKey(10) == ord('q'):
        break

#Release Already Holding Camara
cam.release()

#Distroy All Windows In the Program
cv2.distroyAllWindows()
 
