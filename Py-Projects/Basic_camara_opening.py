import cv2
from datetime import datetime

cap=cv2.VideoCapture(0);
print(cap.isOpened())


while (cap.isOpened()):
    ret, frame=cap.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (10,50), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255,255,255), 5)
    
    cv2.imshow('Image',frame)
    
    if cv2.waitKey(40) & 0xFF ==ord('q'):
        
 
        cap.release()
        cv2.destroyAllWindows()
        break
    
