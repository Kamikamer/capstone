'''
This file is used to test the project with just a webcam and no other tools like tkinter/pygame.
It's purpose is to have a fresh run to be used as a base app and to make sure all other integrated part work together during system testing.
This file can be used for integrated testing as well as unit testing or debugging.
This file is NOT to be used for deployment purposes.
All files in subdirectories are not meant to be used for deployment purposes and only development purposes and should not be ran directly but you can if you want.
'''
import cv2
from posture_fit_algorithm.Gem import ExerciseLogic
from posture_fit_algorithm.Pushup import PushupLogic
from posture_fit_algorithm.Situp import SitupLogic

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

cap = cv2.VideoCapture(0)
cap.set(3,1_000)
cap.set(4,700)
# Change to PushupLogic("Pushup") for pushups
exercise_logic = PushupLogic("Pushup")  
while cap.isOpened():
    cap.set(3,1_300)
    cap.set(4,720)
    response, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # Call the generic process_frame method from Exercise Logic
    exercise_logic.process_frame(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()