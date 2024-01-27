import cv2
# from posture_fit_algorithm.Detector2 import ExerciseLogic
from posture_fit_algorithm.Pushup import PushupLogic
from posture_fit_algorithm.Situp import SitupLogic
# from posture_fit_algorithm.Squads import SquadsLogic
from posture_fit_development.Sound import SoundPlayer
from posture_fit_development.Webcam import ExerciseLogic
import threading
from icecream import ic


time_previous = 0
time_current = 0

class ExerciseHandler:
    def __init__(self):
        self._exercise_logic = None

    @property 
    def exercise_logic(self) -> PushupLogic | SitupLogic |  None:
        return self._exercise_logic

    @exercise_logic.setter # getter
    def exercise_logic(self, logic_type) -> str | None:
        if logic_type == "Pushup":
            self._exercise_logic = PushupLogic("Pushup")
            return "Pushup selected"
        elif logic_type == "Situp":
            self._exercise_logic = SitupLogic("Situp")
            return "Situp selected"
        # Add more logic types as needed dasdasdasda asdasd asdasda asdasd
        else:
            raise ValueError("Invalid logic type")

    def process_frame(self, frame) -> None:
        if self._exercise_logic is not None:
            self._exercise_logic.process_frame(frame)
        else:
            raise ValueError("Exercise logic not set")

if __name__ == "__main__":
    
    print("Starting app")
    sp = SoundPlayer()
    sp.play_sound()
    # webcam = CameraModule()
    # webcam.open_camera()
    cap = cv2.VideoCapture(0)
    exercise_handler = ExerciseHandler()

    exercise_types = ["Situp", "Pushup", "Squats"] 

    for exercise_type in exercise_types:
        try:
            exercise_handler.exercise_logic = exercise_type
        except ValueError as e:
            print(f"Error: {e}")
            continue

        while cap.isOpened():
            response, frame = cap.read()
            frame = cv2.flip(frame, 1)
            exercise_handler.process_frame(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


