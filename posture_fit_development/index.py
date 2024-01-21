import cv2
import mediapipe
import math
class poseDetector() :
    def __init__(self,mode=False,complexity=1,smooth_landmarks=True,enable_segmentation=False,smooth_segmentation=True,detectionCon=0.5,trackCon=0.5):
        self.mode = mode 
        self.complexity = complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mediapipe.solutions.drawing_utils
        self.mpPose = mediapipe.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.complexity,self.smooth_landmarks,self.enable_segmentation,self.smooth_segmentation,self.detectionCon,self.trackCon)
    def findPose(self,img, draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        return img
    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                #finding height, width of the image printed
                h, w, c = img.shape
                #Determining the pixels of the landmarks
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255,0,0), cv2.FILLED)
        return self.lmList
    def findAngle(self, img, p1, p2, p3, draw=True):   
        #Get the landmarks
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]
        #Calculate Angle
        angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))
        if angle < 0:
            angle += 360
            if angle > 180:
                angle = 360 - angle
        elif angle > 180:
            angle = 360 - angle
        #Draw
        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),5)
            cv2.circle(img,(x1,y1),5,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x1,y1),15,(0,0,255),2)
            cv2.putText(img,str(int(angle)),(x2-50,y2+50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        return angle
    def correctForm(self, img, angles, thresholds, draw=True):
        # Check if each angle meets the specified criteria
        is_correct_form = all(abs(angle) >= threshold for angle, threshold in zip(angles, thresholds))
        # Update the color based on correctness
        color = (0, 255, 0) if is_correct_form else (0, 0, 255)
        # Draw the lines and circles with the updated color
        if draw:
            # Specify the landmark indices for the lines you want to draw
            draw_lines_indices = [15, 13, 11, 23, 25]
            for idx in draw_lines_indices:
                if idx < len(self.lmList):
                    lm_id, cx, cy = self.lmList[idx]
                    cv2.circle(img, (cx, cy), 5, color, cv2.FILLED)
                    cv2.circle(img, (cx, cy), 15, color, 2)
            # Draw lines and text annotations for specific landmarks
            for i in range(len(draw_lines_indices) - 1):
                idx1, idx2 = draw_lines_indices[i], draw_lines_indices[i + 1]
                if idx1 < len(self.lmList) and idx2 < len(self.lmList):
                    x1, y1 = self.lmList[idx1][1:]
                    x2, y2 = self.lmList[idx2][1:]
                    # Draw lines
                    cv2.line(img, (x1, y1), (x2, y2), color, 3)
                    # Calculate and display angle
                    angle = self.findAngle(img, idx1, idx2, idx2 + 1, draw=False)
                    cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)
        return is_correct_form
def main():
    detector = poseDetector()
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        response, frame = cap.read()
        frame = cv2.flip(frame,1)    
        if response:    
            frame = detector.findPose(frame)
            cv2.imshow('Pose Detection',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()