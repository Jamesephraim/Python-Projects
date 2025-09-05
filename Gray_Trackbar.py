import cv2


cap=cv2.VideoCapture(0)

def nothing(x):
    pass


cv2.namedWindow('Frame')
cv2.createTrackbar('Gray','Frame',0,10,nothing)
#cv2.createTrackbar('Edges','Frame',0,10,nothing)
#cv2.createTrackbar('Gray','Frame',0,10,nothing)


while True: 
    ret,frame=cap.read()

    gr=cv2.getTrackbarPos('Gray','Frame')
    #edg=cv2.getTrackbarPos('Edges','Frame')

    #cv2.putText(frame,str(gr),(30,60),cv2.FONT_HERSHEY_TRIPLEX,2,(200,0,0))

    if gr==0 :
        pass
    else:
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    

     
    cv2.imshow('Frame',frame)



    if cv2.waitKey(1) == ord('q'):
        break