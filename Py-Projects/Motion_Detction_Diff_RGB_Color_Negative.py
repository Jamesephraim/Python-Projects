import cv2
#Camara Opening
cam=cv2.VideoCapture(0)
#Print Camara Status
print(cam.isOpened())

count=0
#Capture Multiple Frames
while cam.isOpened():

    #Capture Frames 1
    ret, frame1=cam.read()

    #Capture Frames 1
    ret, frame2=cam.read()

    #Capture Difference Between Frames1 & Frame2
    diff=cv2.absdiff(frame1,frame2)

    #Convert Normal Image Frame To Gray Color
    #gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    #Showing The Captured All Frames
    cv2.imshow('WebCam',diff)

    k=cv2.waitKey(10)
    #Inturept if Press 'q' Stop The Captureing Frame into Webcam
    if k == ord('q'):
        break
      
    elif k == ord('s'):
       name="C:/Users/lenovo/Desktop/Python/Py-Projects/Self Images/Motion_Detection_Diff_Negative_{}.png".format(count)
       cv2.imwrite(name,diff)
       print('[+] Ok')

    count+=1

#Release Already Holding Camara
cam.release()
#Distroy All Windows In the Program
cv2.distroyAllWindows()
 
