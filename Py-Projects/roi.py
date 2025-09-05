import cv2


cap=cv2.VideoCapture(0)




while True:
    
    ret,frame=cap.read()
    #         [y1:y2,x1:x2]
    #   |
    #   |y2
    #   |
    #   |
    #   | y1
    #   |___x1_____x2____________
    
   
    #frame=cv2.imread(r"C:\Users\admin\Desktop\MY J2\Best.jpg")
    roi=frame[20:400,200:500]
    cv2.imshow('Roi',roi)
    cv2.imshow('Frame',frame)

    if cv2.waitKey(1) ==ord('q'):
        break
