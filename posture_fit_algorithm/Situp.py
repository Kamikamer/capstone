import cv2
import time
import detector 
from posture_fit_development import Webcam
cap = cv2.VideoCapture(0)
detector = detector.poseDetector()
count = 0
direction = 0
form = 0
time_previous = 0
time_current = 0
feedback = "Fix Form"
frame = Webcam().camera_stats()
while cap.isOpened():
    img = detector.findPose(frame,False)
    lmList = detector.findPosition(frame,False)
    if len(lmList) != 0:
        knee = detector.findAngle(frame,23,25,27,draw=False)
        hip = detector.findAngle(frame,11,23,25,draw=False)
        ankle = detector.findAngle(frame,25,27,31,draw=False)        
        # Specify the angles and thresholds for correctness
        angles = [hip,knee,ankle]
        thresholds = [140,85,130]
        # Use the correctForm function to check and draw lines with correct color
        is_correct_form = detector.correctForm(frame,angles,thresholds)
        if is_correct_form:
            form = 1
        if form == 1:
            if ankle <= 135 and knee <= 90 and hip >= 145:
                feedback = "Down"
                if direction == 0:
                    count += 0.5
                    direction = 1
            else:
                feedback = "Fix Form"
            if ankle <= 135 and knee <= 90 and hip <= 35:
                feedback = "Down"
                if direction == 1:
                    count += 0.5
                    direction = 0
            else:
                feedback = "Fix Form"
        #Situp counter and frame rate
        cv2.rectangle(frame,(0,380),(100,480),(0,0,0),cv2.FILLED)
        cv2.putText(frame,str(int(count)),(25,455),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
    cv2.imshow('Situp counter',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()