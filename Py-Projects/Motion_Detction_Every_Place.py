import cv2
 
cam=cv2.VideoCapture(0)
print(cam.isOpened())


count=0
while cam.isOpened():
     ret, frame1=cam.read()
     ret, frame2=cam.read()
     frame1=cv2.resize(frame1,(500,500))
     frame2=cv2.resize(frame2,(500,500))
      
     #calculate difference between frame1 and frame2
     diff=cv2.absdiff(frame1,frame2)
     
     #convert rgb image to gray coloring
     gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
     #gray=gray[300:400,200:300]

     #print(gray)
     #Remove small distabences
     _,thresh=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
     dilated=cv2.dilate(thresh,None,iterations=3)

     #All moving is selected
     #findContours(img,contour_retrival_mode,method)
     contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
     #After select All moving Area Is Blink
     #drawContours(img,contours,id of contours,color,thickness)
     #cv2.drawContours(frame1,contours,-1,(0,255,0),2)


     for c in contours:
          if cv2.contourArea(c) < 5000:
               continue
          x,y,w,h=cv2.boundingRect(c)
          cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),6)
          name="C:/Users/lenovo/Desktop/Python/Py-Projects/Motion_Detection_Images/Image_{}.png".format(count)
          print('[+] Image Saved Successfully')
          count+=1
          cv2.imwrite(name,frame1)
     #frame1=frame1[100:300+20,50:500+25]     
     cv2.imshow('WebCam',frame1)
     if cv2.waitKey(10) == ord('q'):
        break
   
cam.release()
 
 
