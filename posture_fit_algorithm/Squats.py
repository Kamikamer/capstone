from posture_fit_algorithm.Gem import ExerciseLogic
from posture_fit_development.Sound import SoundPlayer
class SquatsLogic(ExerciseLogic):
    def __init__(self, exercise_name) -> None:
        super().__init__(exercise_name=exercise_name, sound_type="IF_1")
        self.prev_form_correct = True

    def get_angles_and_thresholds(self, frame) -> tuple[list[float], list[int]]:
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)
        # Specify the angles and thresholds for correctness
        angles = [hip,knee]
        thresholds = [160,150]
        return angles, thresholds
    
    def process_specific_angles(self, frame) -> None:
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)
        if knee > 170 and hip > 170:
            self.feedback = "Up"
            if self.direction == 0:
                self.count += 0.5
                self.direction = 1

        if knee > 150 and hip > 30:
            self.feedback = "Down"
            if self.direction == 1:
                self.count += 0.5
                self.direction = 0


    def process_frame(self, frame) -> None:
        return super().process_frame(frame=frame)