import cv2
#import winsound

cam=cv2.VideoCapture(0)
print(cam.isOpened())

while cam.isOpened():
     
     ret, frame1=cam.read()
     ret, frame2=cam.read()
     #roi= frame1[20:300,200:400]
     #calculate difference between frame1 and frame2
     diff=cv2.absdiff(frame1,frame2)
     
     #convert rgb image to gray coloring
     gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
     
     #Remove small distabences
     _,thresh=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
     dilated=cv2.dilate(thresh,None,iterations=3)

     #All moving is selected
     contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
     #After select All moving Area Is Blink 
     #cv2.drawContours(frame1,contours,-1,(0,255,0),2)


     for c in contours:
          if cv2.contourArea(c) < 5000:
               continue
          
          x,y,w,h=cv2.boundingRect(c)
          
          #cv2.rectangle(img_frame,(Starting_x,Starting_Y),(Ending_x,Ending_Y),(Color),Thickness)         
          cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)
          
          #cv2.circle(img_frame,(Starting_x,Starting_Y),size,(Color),Thickness)
          #cv2.circle(frame1,(x,y),60,(0,0,255),5)
          #cv2.putText(Img-frame,'Text',(staring_X,Starting_Y),Font_style,FontSize,color,Thickness)

          font=cv2.FONT_ITALIC
          #Insert text in Output Window
          cv2.putText(frame1,'--Motion--',(20,60),font,1,(0,0,255),2)
          
          #if Any Object can Move Mke A Noise
          #winsound.Beep(3377,500)
     #roi= frame1[20:300,200:400]   
     #cv2.imshow('ROI',roi)
     cv2.imshow('WebCam',frame1)
     
     if cv2.waitKey(1) == ord('q'):
        break
     
cam.release()

 
