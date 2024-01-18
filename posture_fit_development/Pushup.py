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
    frame = cv2.flip(frame,1)
    frame_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    time_current = time.time()
    fps = 1 / (time_current - time_previous)
    time_previous = time_current
    img = detector.findPose(frame,False)
    lmList = detector.findPosition(frame,False)
    if len(lmList) != 0:
        elbow = detector.findAngle(frame,11,13,15,draw=False)
        shoulder = detector.findAngle(frame,13,11,23,draw=False)
        hip = detector.findAngle(frame,11,23,25,draw=False)
        # Specify the angles and thresholds for correctness
        angles = [elbow,shoulder,hip]
        thresholds = [155,35,155]
        # Use the correctForm function to check and draw lines with correct color
        is_correct_form = detector.correctForm(frame,angles,thresholds)
        if is_correct_form:
            form = 1
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
        cv2.rectangle(frame,(0,380),(100,480),(0,0,0),cv2.FILLED)
        cv2.putText(frame,str(int(count)),(25,455),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
        cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
    cv2.imshow('Pushup counter',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()