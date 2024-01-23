import cv2
from posture_fit_algorithm.Detector2 import ExerciseLogic
from posture_fit_algorithm.Pushup import PushupLogic  # noqa: F401
from posture_fit_algorithm.Situp import SitupLogic
from posture_fit_algorithm.Squads import SquadsLogic
from icecream import ic
cap = cv2.VideoCapture(0)
# Change to PushupLogic("Pushup") for pushups
exercise_logic = SitupLogic("Situp")  
while cap.isOpened():
    response, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # Call the generic process_frame method from Exercise Logic
    exercise_logic.process_frame(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()