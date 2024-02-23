from typing import NamedTuple, NoReturn
import cv2
import math
import time
import traceback
import threading
from posture_fit_development.Sound import SoundPlayer
import mediapipe as mp
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa
class ExerciseLogic:
    def __init__(self, exercise_name: str, sound_type: str) -> None:
        self.exercise_name = exercise_name
        self._setup_variables()
        self._setup_sound_player(sound_type=sound_type)
        self._setup_mppose()
        try:
            ic.configureOutput(prefix=f'{self.exercise_name} Logic (ツ)_/¯ ', includeContext=True)
        except AttributeError:
            pass
    def _setup_sound_player(self, sound_type) -> None:
        self.sound_type: str = sound_type
        self.sp = SoundPlayer()    
    def _setup_mppose(self) -> None:
        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mpPose.Pose(static_image_mode=False, model_complexity=1, smooth_landmarks=True, enable_segmentation=False, smooth_segmentation=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)
    def _setup_variables(self) -> None:
        self.form: int = 0
        self.direction: int = 0
        self.fps: float = 0
        self.count: float = 0
        self.time_previous: float = 0
        self.feedback: str | None = None
        self.lmList: list = []
        self.fps_history: list[int | float] = []
        self.results: NamedTuple | None = None
    def play_sound_async(self) -> None | NoReturn:
        try:
            self.sp.play_sound(self.sound_type)
        except Exception as e:
            print("Error playing sound: ", e)
            print(traceback.format_exc())
            print("-" * 50)
            raise e       
    def update_fps_time(self) -> float:
        time_current: float = time.time()
        fps: float = 1 / (time_current - self.time_previous)
        self.time_previous: float = time_current
        self.fps: float = fps
        return fps
    def process_frame(self, frame):
        _ = self.update_fps_time() # Updates self.fps
        img = self.findPose(frame, False)
        lmList = self.findPosition(frame, False)
        angles, thresholds = self.get_angles_and_thresholds(frame)
        if len(lmList) != 0:
            is_correct_form = self.correctForm(frame, angles, thresholds)
            if is_correct_form:
                self.form = 1
            if self.form == 1:
                self.process_specific_angles(frame)
            cv2.rectangle(frame,(370,400),(0,490),(255,255,255),cv2.FILLED)
            if self.exercise_name == 'Pushup':
                cv2.putText(frame,'pushup', (10, 440), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)
            if self.exercise_name == 'Squats':
                cv2.putText(frame,'squats', (10, 440), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)
            if self.exercise_name == 'Crunch':
            cv2.putText(frame, f'counter : {int(self.count):03d}', (10, 480), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)
            cv2.putText(frame, f'fps : {str(int(self.fps))}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:  # pytype: disable=attribute-error # type: ignore
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)  # pytype: disable=attribute-error # type: ignore
        return img
    def findPosition(self, img, draw=True) -> list:
        self.lmList = []
        if self.results.pose_landmarks: # type: ignore
            for id, lm in enumerate(self.results.pose_landmarks.landmark): # type: ignore
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList
    def findAngle(self, img, p1, p2, p3, draw=True) -> float:
        if len(self.lmList) >= max(p1, p2, p3) + 1:  # Check if the list has enough elements
            x1, y1 = self.lmList[p1][1:]
            x2, y2 = self.lmList[p2][1:]
            x3, y3 = self.lmList[p3][1:]
            # Calculate angle using atan2
            angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
            # Normalize angle to be within [0, 360) degrees
            angle = angle % 360
            # Ensure angle is within [0, 180) degrees
            if angle >= 180:
                angle = 360 - angle
            if draw:
                # Draw lines and circles on the image
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 5)
                cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
                cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            return angle
        else:
            return 0.0  # Return default angle if the list doesn't have enough elements
    def correctForm(self, img, angles, thresholds, draw=True) -> bool:
        is_correct_form = all(abs(angle) < threshold for angle, threshold in zip(angles, thresholds))
        # print(angles) # 23, 166, 178
        # if self.exercise_name == "Squats":
        # for angle, threshold in zip(angles, thresholds):
        #     if abs(angle) > threshold:
        #         print(angle, threshold) 
        # for angle, threshold in zip(angles, thresholds):
        #     print(angle)
        color = (0, 255, 0) if is_correct_form else (0, 0, 255)
        # Check if there's a change from correct to incorrect form
        if self.prev_form_correct and not is_correct_form:
            threading.Thread(target=self.play_sound_async).start()
            self.prev_form_correct = False  # Update the previous form state
        # Update previous form state
        self.prev_form_correct = is_correct_form
        if draw:
            draw_lines_indices = [13, 11, 23, 25,27]
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