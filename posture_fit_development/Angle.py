import cv2
import mediapipe
import numpy
import time
import pr
cap = cv2.VideoCapture(0)
detector = pr.poseDetector()
while cap.isOpened():
    response, frame = cap.read()
    #frame_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
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

    cv2.imshow('Angle',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()