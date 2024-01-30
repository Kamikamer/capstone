from posture_fit_algorithm.Detector2 import ExerciseLogic
from posture_fit_development.Sound import SoundPlayer
class SquatsLogic(ExerciseLogic):
    def __init__(self, exercise_name) -> None:
        super().__init__(exercise_name=exercise_name, sound_type="IF_1")

    def get_angles_and_thresholds(self, frame) -> tuple[list[float], list[int]]:
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)
        # Specify the angles and thresholds for correctness
        angles = [hip,knee]
        thresholds = [140,85]
        return angles, thresholds
    
    def process_specific_angles(self, frame) -> None:
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)
        if knee >= 100 and hip >= 145:
            self.feedback = "Up"
            if self.direction == 0:
                self.count += 0.5
                self.direction = 1
        else:
            self.feedback = "Fix Form"
        if knee < 100 and hip < 100:
            self.feedback = "Down"
            if self.direction == 1:
                self.count += 0.5
                self.direction = 0
        else:
            self.feedback = "Fix Form"

    def process_frame(self, frame) -> None:
        return super().process_frame(frame=frame)