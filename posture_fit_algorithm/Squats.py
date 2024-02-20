from posture_fit_algorithm.Gem import ExerciseLogic
class SquatsLogic(ExerciseLogic):
    def __init__(self, exercise_name) -> None:
        super().__init__(exercise_name=exercise_name, sound_type="IF_1")
        self.prev_form_correct = True
    def get_angles_and_thresholds(self, frame) -> tuple[list[float], list[int]]:
        shoulder = self.findAngle(frame,13,11,23,draw=False)
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)
        # Specify the angles and thresholds for correctness
        angles = [shoulder,hip,knee]
        thresholds = [90,178,178]
        return angles, thresholds
    def process_specific_angles(self, frame) -> None:
        shoulder = self.findAngle(frame,13,11,23,draw=False)
        knee = self.findAngle(frame,23,25,27,draw=False)
        hip = self.findAngle(frame,11,23,25,draw=False)
        if knee > 160 and hip > 160:
            self.feedback = "Up"
            if self.direction == 0:
                self.count += 0.5
                self.direction = 1
        elif knee < 50 and hip < 50:
            self.feedback = "Down"
            if self.direction == 1:
                self.count += 0.5
                self.direction = 0
        else:
            self.count += 0
        print(f'{knee:.0f}')
        print(f'{hip:.0f}')
        print(f'{shoulder:.0f}')
    def process_frame(self, frame) -> None:
        return super().process_frame(frame=frame)
        # 100, 100, 85, 85