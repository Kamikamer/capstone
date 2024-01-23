from posture_fit_algorithm.Detector2 import ExerciseLogic
from posture_fit_development.Sound import SoundPlayer
class SquadsLogic(ExerciseLogic):
    def get_angles_and_thresholds(self, frame) -> tuple[list[int], list[int]]:
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)
        # Specify the angles and thresholds for correctness
        angles = [knee,hip]
        thresholds = [85,165]
        return angles, thresholds
    def process_specific_angles(self, frame) -> None:
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)
        if knee > 170 and hip >= 170:
            self.feedback = "Up"
            if self.direction == 0:
                self.count += 0.5
                self.direction = 1
        else:
            self.feedback = "Fix Form"
            sp = SoundPlayer()
            sp.play_sound()
        if knee < 90 and hip > 60:
            self.feedback = "Down"
            if self.direction == 1:
                self.count += 0.5
                self.direction = 0
        else:
            self.feedback = "Fix Form"
            sp = SoundPlayer()
            sp.play_sound()