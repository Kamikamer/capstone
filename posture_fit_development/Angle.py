import cv2
import posture_fit_algorithm.detector as detector
cap = cv2.VideoCapture(0)
detector = detector.poseDetector()
while cap.isOpened():
    response, frame = cap.read()
    frame = cv2.flip(frame,1)    
    frame = detector.findPose(frame,False)
    lmList = detector.findPosition(frame,False)
    if len(lmList) != 0:
            elbow = detector.findAngle(frame,12,14,16)
            shoulder = detector.findAngle(frame,14,12,24)
            hip = detector.findAngle(frame,12,24,26)
            knee = detector.findAngle(frame,24,26,28)
            wrist = detector.findAngle(frame,14,16,20)
            ankle = detector.findAngle(frame,26,28,30)
    cv2.imshow('Angle',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()