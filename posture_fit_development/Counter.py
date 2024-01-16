import cv2
import mediapipe
import numpy
import time
import pr
cap = cv2.VideoCapture(0)
detector = pr.poseDetector()
count = 0
while cap.isOpened():
    response, frame = cap.read()
    #frame_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    ret, img = cap.read() #640 x 480
    #Determine dimensions of video - Help with creation of box in Line 43
    width  = cap.get(3)  # float `width`
    height = cap.get(4)  # float `height`
    # print(width, height)   
    img = detector.findPose(img,False)

    cv2.rectangle(img,(0,380),(120,480),(0,0,0),cv2.FILLED)
    cv2.putText(img,str(int(count)),(25,455),cv2.FONT_HERSHEY_PLAIN, 5,(255,255,255),5)
    cv2.imshow('Pushup counter',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()