import cv2
face_cascade=cv2.CascadeClassifier(r'/home/ubentu/Desktop/My Project/xml/haarcascade_eye_tree_eyeglasses.xml')


cap=cv2.VideoCapture(0)

#img=cv2.imread('friends.png')
while True:
    _, img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)

    i=0
    for (x,y,w,h) in faces:
    
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("Image",img)
        k=cv2.waitKey(30) &0xff
        i=i+1
        if k==32:
            break
        print(i)
cap.release()
    

