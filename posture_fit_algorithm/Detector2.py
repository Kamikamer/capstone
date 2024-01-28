import cv2
import posture_fit_algorithm.Detector as Detector
import mediapipe
import math
import time
from icecream import ic

class ExerciseLogic:
    def __init__(self, exercise_name):
        self.exercise_name = exercise_name
        self.mpDraw = mediapipe.solutions.drawing_utils
        self.mpPose = mediapipe.solutions.pose
        self.pose = self.mpPose.Pose()
        self.count = 0
        self.direction = 0
        self.form = 0
        self.time_previous = 0
        self.feedback = "Fix Form"
        self.lmList = []

    def process_frame(self, frame):
        frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        time_current = time.time()
        fps = 1 / (time_current - self.time_previous)
        self.time_previous = time_current

        img = self.findPose(frame, False)
        self.lmList = self.findPosition(frame, False)
        ic("Huh")
        angles, thresholds = self.get_angles_and_thresholds(frame)

        if len(self.lmList) != 0:
            is_correct_form = self.correctForm(frame, angles, thresholds)

            if is_correct_form:
                self.form = 1

            if self.form == 1:
                self.process_specific_angles(frame)

            cv2.rectangle(frame, (0, 380), (100, 480), (0, 0, 0), cv2.FILLED)
            cv2.putText(frame, str(int(self.count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
            cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

        cv2.imshow(f'{self.exercise_name} counter', frame)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True) -> list:
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList

    def findAngle(self, img, p1, p2, p3, draw=True):
        print("="*10)
        ic(self.lmList)
        print("="*10)
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
            if angle > 180:
                angle = 360 - angle
        elif angle > 180:
            angle = 360 - angle
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 5)
            cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle

    def correctForm(self, img, angles, thresholds, draw=True):
        is_correct_form = all(abs(angle) >= threshold for angle, threshold in zip(angles, thresholds))
        color = (0, 255, 0) if is_correct_form else (0, 0, 255)
        draw_lines_indices = [15, 13, 11, 23, 25]
        for idx in draw_lines_indices:
            if idx < len(self.lmList):
                lm_id, cx, cy = self.lmList[idx]
                cv2.circle(img, (cx, cy), 5, color, cv2.FILLED)
                cv2.circle(img, (cx, cy), 15, color, 2)
        for i in range(len(draw_lines_indices) - 1):
            idx1, idx2 = draw_lines_indices[i], draw_lines_indices[i + 1]
            if idx1 < len(self.lmList) and idx2 < len(self.lmList):
                x1, y1 = self.lmList[idx1][1:]
                x2, y2 = self.lmList[idx2][1:]
                cv2.line(img, (x1, y1), (x2, y2), color, 3)
                angle = self.findAngle(img, idx1, idx2, idx2 + 1, draw=False)
                cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)
        return is_correct_form
    
    def get_angles_and_thresholds(self, frame) -> tuple[list[float], list[int]]:
        raise NotImplementedError
    
    def process_specific_angles(self, frame) -> None:
        raise NotImplementedError