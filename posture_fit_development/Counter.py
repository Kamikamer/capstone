import cv2
import posture_fit_algorithm.detector as detector
cap = cv2.VideoCapture(0)
detector = detector.poseDetector()
count = 0
while cap.isOpened():
    response, frame = cap.read()
    frame = cv2.flip(frame,1)    
    frame = detector.findPose(frame,False)
    cv2.rectangle(frame,(0,380),(120,480),(0,0,0),cv2.FILLED)
    cv2.putText(frame,str(int(count)),(25,455),cv2.FONT_HERSHEY_PLAIN, 5,(255,255,255),5)
    cv2.imshow('Pushup counter',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()