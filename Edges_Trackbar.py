import cv2

#/home/ubentu/Videos/road7.mp4
path=0
cap=cv2.VideoCapture(path)

def nothing(x):
    pass


cv2.namedWindow('Frame')
cv2.createTrackbar('one','Frame',0,255,nothing)
cv2.createTrackbar('two','Frame',0,255,nothing)
#cv2.createTrackbar('Gray','Frame',0,10,nothing)


while True: 
    ret,frame=cap.read()
    if not ret:
        cap=cv2.VideoCapture(path)
        continue
    frame=cv2.resize(frame,(600,400))
    one=cv2.getTrackbarPos('one','Frame')
    two=cv2.getTrackbarPos('two','Frame')
     



    #edg=cv2.getTrackbarPos('Edges','Frame')
    #edges=cv2.Canny(gray,400,300)
    cv2.putText(frame,str(one),(30,60),cv2.FONT_HERSHEY_TRIPLEX,2,(200,0,0))
    cv2.putText(frame,str(two),(30,120),cv2.FONT_HERSHEY_TRIPLEX,2,(200,0,0))


    if one==0 :
        pass
    else:
        frame=cv2.Canny(frame,one,two)
    

     
    cv2.imshow('Frame',frame)



    if cv2.waitKey(1) == ord('q'):
        break