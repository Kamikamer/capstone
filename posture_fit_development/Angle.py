import cv2
import mediapipe
import numpy
import time
import index
cap = cv2.VideoCapture(0)
detector = index.poseDetector()
while cap.isOpened():
    response, frame = cap.read()
    frame = detector.findPose(frame,False)
    lmList = detector.findPosition(frame,False)
    if len(lmList) != 0:
        elbow = detector.findAngle(frame,11,13,15)
        shoulder = detector.findAngle(frame,13,11,23)
        hip = detector.findAngle(frame,11,23,25)
    cv2.imshow('Angle',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()