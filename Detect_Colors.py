import cv2
import numpy as np
import time

#'/home/ubentu/Videos/road7.mp4'
#path=str(input('Enter Cam ID or Video Path ---> :'))
path=0
def detect_colors():
    cap=cv2.VideoCapture(path)
    name='Filters'
    print(path)
    print(cap.isOpened())

    def nothing(x):
        pass

    
    cv2.namedWindow(name)
    cv2.createTrackbar('LH',name,0,255,nothing)
    cv2.createTrackbar('LS',name,0,255,nothing)
    cv2.createTrackbar('LV',name,0,255,nothing)
    cv2.createTrackbar('UH',name,255,255,nothing)
    cv2.createTrackbar('US',name,255,255,nothing)
    cv2.createTrackbar('UV',name,255,255,nothing)
 

    while True:
        #frame=cv2.imread('/home/ubentu/Desktop/My Project/Images/save.jpg')
        ret,frame=cap.read()
        if not ret:
            cap=cv2.VideoCapture(path)
            continue

        frame=cv2.resize(frame,(400,340))
        #convert hsv
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


        l_h=cv2.getTrackbarPos('LH',name,)
        l_s=cv2.getTrackbarPos('LS',name,)
        l_v=cv2.getTrackbarPos('LV',name,) 
        u_h=cv2.getTrackbarPos('UH',name,)
        u_s=cv2.getTrackbarPos('US',name,)
        u_v=cv2.getTrackbarPos('UV',name,)

        #Detect Blue Color in Present Frame
        
        l_b=np.array([l_h,l_s,l_v])
        u_b=np.array([u_h,u_s,u_v])

        mask=cv2.inRange(hsv,l_b,u_b)
        edges=cv2.Canny(mask,200,250)

        res=cv2.bitwise_and(frame,frame,mask=mask)
        #lines=cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength=100,maxLineGap=10)
        
        #lines=cv2.HoughLinesP(mask,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

        #if lines is not None:
        #    for line in lines:
        #        x1,y1,x2,y2 = line[0]
        #       cv2.line(frame,(x1,y1),(x2,y2),(0,0,200),2)
        #        cv2.line(res,(x1,y1),(x2,y2),(0,0,200),2)


        cv2.imshow('Frame',frame)
        cv2.imshow('Filters',res)
        cv2.imshow('Mask',mask)




        if cv2.waitKey(50) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return



def detect_lines():
    cap=cv2.VideoCapture(path)
    name='Filters'
    print(path)
    print(cap.isOpened())

    def nothing(x):
        pass

    
    cv2.namedWindow(name)
    cv2.createTrackbar('LH',name,0,255,nothing)
    cv2.createTrackbar('LS',name,0,255,nothing)
    cv2.createTrackbar('LV',name,0,255,nothing)
    cv2.createTrackbar('UH',name,255,255,nothing)
    cv2.createTrackbar('US',name,255,255,nothing)
    cv2.createTrackbar('UV',name,255,255,nothing)



    while True:
        #frame=cv2.imread('/home/ubentu/Desktop/My Project/Images/save.jpg')
        ret,frame=cap.read()
        if not ret:
            cap=cv2.VideoCapture(path)
            continue

        frame=cv2.resize(frame,(400,340))
        #convert hsv
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


        l_h=cv2.getTrackbarPos('LH',name,)
        l_s=cv2.getTrackbarPos('LS',name,)
        l_v=cv2.getTrackbarPos('LV',name,) 
        u_h=cv2.getTrackbarPos('UH',name,)
        u_s=cv2.getTrackbarPos('US',name,)
        u_v=cv2.getTrackbarPos('UV',name,)

        #Detect Blue Color in Present Frame
        
        l_b=np.array([l_h,l_s,l_v])
        u_b=np.array([u_h,u_s,u_v])

        mask=cv2.inRange(hsv,l_b,u_b)
        edges=cv2.Canny(mask,200,250)

        res=cv2.bitwise_and(frame,frame,mask=mask)
        #lines=cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength=100,maxLineGap=10)
        
        lines=cv2.HoughLinesP(mask,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

        if lines is not None:
            for line in lines:
                x1,y1,x2,y2 = line[0]
                cv2.line(frame,(x1,y1),(x2,y2),(0,0,200),2)
                cv2.line(res,(x1,y1),(x2,y2),(0,0,200),2)


        cv2.imshow('Frame',frame)
        cv2.imshow('Filters',res)
        cv2.imshow('Mask',mask)




        if cv2.waitKey(50) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return


while True:
    print('\t---------------------------------------')
     
    print('\t\t[1] Detect Colors')
    print('\t\t[2] Detect Lines')
    print('\t\t[0] Exit')
    print('\t---------------------------------------')


    key=int(input('\t\t[+] Enter Choice :'))

    if key==1:
        detect_colors()
    elif key==2:
        detect_lines()
    elif key==0:
        exit()
    else: 
        print('Invalid Input')
        time.sleep(2)
