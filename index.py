import cv2
from icecream import ic
import time
from posture_fit_algorithm.Pushup import PushupLogic

time_previous = 0
time_current = 0

if __name__ == "__main__":
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)
    
    exercise_logic = PushupLogic("Pushup")
    while cap.isOpened():
        response, frame = cap.read()
        exercise_logic.process_frame(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

