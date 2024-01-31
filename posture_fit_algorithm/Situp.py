from posture_fit_algorithm.Detector2 import ExerciseLogic
from posture_fit_development.Sound import SoundPlayer
class SitupLogic(ExerciseLogic):
    def __init__(self, exercise_name) -> None:
        super().__init__(exercise_name=exercise_name, sound_type="IF_1")
        self.prev_form_correct = True        

    def get_angles_and_thresholds(self, frame) -> tuple[list[float], list[int]]:
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)


        # Specify the angles and thresholds for correctness
        angles = [hip,knee]
        thresholds = [110,100]
        return angles, thresholds
    
    def process_specific_angles(self, frame) -> None:
        knee = self.findAngle(frame, 23, 25, 27, draw=False)
        hip = self.findAngle(frame, 11, 23, 25, draw=False)

        if knee > 90 and hip > 100:
            self.feedback = "Up"
            if self.direction == 0:
                self.count += 0.5
                self.direction = 1
        else:
            self.feedback = "Fix Form"
            
        if knee < 85 and hip < 90 :
            self.feedback = "Down"
            if self.direction == 1:
                self.count += 0.5
                self.direction = 0
        else:
            self.feedback = "Fix Form"
            # sp = SoundPlayer()
            # sp.play_sound()
