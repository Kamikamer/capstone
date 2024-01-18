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
        knee = detector.findAngle(img, 23, 25, 27, draw=False)
        hip = detector.findAngle(img, 11, 23, 25, draw=False)
        # Specify the angles and thresholds for correctness
        angles = [knee, hip]
        thresholds = [155, 35, 155]
        # Use the correctForm function to check and draw lines with correct color
        is_correct_form = detector.correctForm(img, angles, thresholds)
        if is_correct_form:
            form = 1
        if form == 1:
                if knee <= 90 and hip > 160:
                        feedback = "Up"
                        if direction == 0:
                            count += 0.5
                            direction = 1
                else:
                    feedback = "Fix Form"
                if knee > 160 and hip > 160:
                    feedback = "Down"
                    if direction == 1:
                         count += 0.5
                         direction = 0
                else:
                     feedback = "Fix Form"
        #Pushup counter
        cv2.rectangle(img,(0,380),(100,480),(0,0,0),cv2.FILLED)
        cv2.putText(img,str(int(count)),(25,455),cv2.FONT_HERSHEY_PLAIN, 3,(255,255,255),3)
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
    cv2.imshow('Pushup counter',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()