import cv2
import mediapipe
import numpy
import time
import pr
cap = cv2.VideoCapture(0)
detector = pr.poseDetector()
count = 0
direction = 0
form = 0
time_previous = 0
time_current = 0
feedback = "Fix Form"
while cap.isOpened():
    response, frame = cap.read()
    frame_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    time_current = time.time()
    fps = 1 / (time_current - time_previous)
    time_previous = time_current
    ret, img = cap.read() #640 x 480
    #Determine dimensions of video - Help with creation of box in Line 43
    width  = cap.get(3)  # float `width`
    height = cap.get(4)  # float `height`
    # print(width, height)   
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    # print(lmList)
    if len(lmList) != 0:
        elbow = detector.findAngle(img,11,13,15)
        shoulder = detector.findAngle(img,13,11,23)
        hip = detector.findAngle(img,11,23,25)
        #Check to ensure right form before starting the program
        if elbow > 160 and shoulder > 40 and hip > 160:
            form = 1
        #Check for full range of motion for the pushup
        if form == 1:
                if elbow <= 90 and hip > 160:
                    feedback = "Up"
                    if direction == 0:
                        count += 0.5
                        direction = 1
                else:
                    feedback = "Fix Form"
                if elbow > 160 and shoulder > 40 and hip > 160:
                    feedback = "Down"
                    if direction == 1:
                        count += 0.5
                        direction = 0
                else:
                    feedback = "Fix Form"
        #Pushup counter
        cv2.rectangle(img,(0,380),(100,480),(0,0,0),cv2.FILLED)
        cv2.putText(img,str(int(count)),(25,455),cv2.FONT_HERSHEY_PLAIN, 5,(255,255,255),5)
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
    cv2.imshow('Pushup counter',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()