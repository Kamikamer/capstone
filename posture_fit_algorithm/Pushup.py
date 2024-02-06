from posture_fit_algorithm.Gem import ExerciseLogic
from posture_fit_development.Sound import SoundPlayer
import threading

class PushupLogic(ExerciseLogic):
    def __init__(self, exercise_name, sound_type="IF_1") -> None:
        super().__init__(exercise_name=exercise_name, sound_type=sound_type)
        self.prev_form_correct = True

    def get_angles_and_thresholds(self, frame) -> tuple[list[float], list[int]]:
        elbow = self.findAngle(frame, 11, 13, 15, draw=False)
        shoulder = self.findAngle(frame, 13, 11, 23, draw=False)
        hip = self.findAngle(frame, 11, 23, 25, draw=False)
        # Specify the angles and thresholds for correctness
        angles = [elbow, shoulder, hip]     
        thresholds = [180,90,180]
        return angles, thresholds
    

    def process_specific_angles(self, frame) -> None:
        elbow = self.findAngle(frame, 11, 13, 15, draw=False)
        shoulder = self.findAngle(frame, 13, 11, 23, draw=False)
        hip = self.findAngle(frame, 11, 23, 25, draw=False)
        if elbow <= 90 and hip >= 160:
            self.feedback = "Up"
            if self.direction == 0:
                self.count += 0.5
                self.direction = 1
            else:
                self.feedback = "Fix Form"
                
        if elbow >= 160 and shoulder >= 40 and hip >= 160:
            self.feedback = "Down"
            if self.direction == 1:
                self.count += 0.5
                self.direction = 0
            else:
                self.feedback = "Fix Form"

    def process_frame(self, frame) -> None:
        return super().process_frame(frame=frame)