from posture_fit_algorithm.Detector2 import ExerciseLogic
from posture_fit_development.Sound import SoundPlayer
class SitupLogic(ExerciseLogic):
    def get_angles_and_thresholds(self, frame) -> tuple[list[int], list[int]]:
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)
        ankle = self.findAngle(frame,25,27,29,draw=False)
        # Specify the angles and thresholds for correctness
        angles = [hip,knee,ankle]
        thresholds = [140,85,130]
        return angles, thresholds
    def  process_specific_angles(self, frame) -> None:
        ankle = self.findAngle(frame, 25, 27, 29, draw=False)
        knee = self.findAngle(frame, 23, 25, 27, draw=False)
        hip = self.findAngle(frame, 11, 23, 25, draw=False)
        if ankle <= 135 and knee <= 90 and hip >= 145:
            self.feedback = "Down"
            if self.direction == 0:
                self.count += 0.5
                self.direction = 1
        else:
            self.feedback = "Fix Form"
            sp = SoundPlayer()
            sp.play_sound()
        if ankle <= 135 and knee <= 90 and hip <= 35:
            self.feedback = "Down"
            if self.direction == 1:
                self.count += 0.5
                self.direction = 0
        else:
            self.feedback = "Fix Form"
            sp = SoundPlayer()
            sp.play_sound()
