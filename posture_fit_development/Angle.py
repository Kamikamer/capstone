import cv2

cap = cv2.VideoCapture(0)
while cap.isOpened():
    response, frame = cap.read()
    frame = cv2.flip(frame,1)    
    frame = Detector.findPose(frame,False)
    lmList = Detector.findPosition(frame,False)
    if len(lmList) != 0:
            elbow = Detector.findAngle(frame,12,14,16)
            shoulder = Detector.findAngle(frame,14,12,24)
            hip = Detector.findAngle(frame,12,24,26)
            knee = Detector.findAngle(frame,24,26,28)
            wrist = Detector.findAngle(frame,14,16,20)
            ankle = Detector.findAngle(frame,26,28,30)
    cv2.imshow('Angle',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()