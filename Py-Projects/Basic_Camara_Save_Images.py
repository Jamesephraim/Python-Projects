import cv2

cam=cv2.VideoCapture(0)

print(cam.isOpened())
print("[-] Press 'q' to Exit")
print("[-] Press 's' to Capture Images ")
#print("[+] How many Images Can Save :")
#count=int(input())


count=0


while True:
    
    _,frame=cam.read()

    

    #cv2.imshow('TEST',frame)
    i=cv2.waitKey(1)
    if i == ord('q'):
        print("[-] Exit")
        break
    
    elif i == ord('s'):
       name="MyPic_{}.png".format(count)
       cv2.imwrite(name,frame)
       print('[+] Ok')
       #key=key+1
       count+=1
       
    elif count==2:
       break
    


    cam.release()
     
