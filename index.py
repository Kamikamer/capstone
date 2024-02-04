from typing import Literal
import cv2
from posture_fit_algorithm.Pushup import PushupLogic
from posture_fit_algorithm.Squats import SquatsLogic
from posture_fit_algorithm.Situp import SitupLogic
# from posture_fit_algorithm.Detector2 import ExerciseLogic
from posture_fit_development.Sound import SoundPlayer
# from posture_fit_algorithm.Squads import SquadsLogic
# from posture_fit_development.Webcam import ExerciseLogic
import threading
from icecream import ic
import cv2
import time
import tkinter as tk
from tkinter import messagebox


time_previous = 0
time_current = 0

# def push_up_counter():
#     cap = cv2.VideoCapture(0)
#     exercise_logic = Pushup.PushupLogic("Pushup")
#     while cap.isOpened():
#         _, frame = cap.read()
#         frame = cv2.flip(frame, 1)
#         exercise_logic.process_frame(frame)
#     cap.release()
#     cv2.destroyAllWindows()

# def start_push_up_counter():
#     messagebox.showinfo("Pushup Counter", "Pushup Counter will start. Press 'q' to exit.")
#     push_up_counter()

if __name__ == "__main__":
    # root = tk.Tk()
    # root.title("Pushup Counter")

    # start_button = tk.Button(root, text="Start Pushup Counter", command=start_push_up_counter)
    # start_button = tk.Button(root, text="Start Situps Counter", command=start_push_up_counter)
    # # start_button = tk.Button(root, text="Start Pushup Counter", command=start_push_up_counter)
    # start_button.pack(pady=20)

    # root.mainloop()

    cap = cv2.VideoCapture(0)
    exercise_logic = SitupLogic("Situp", "IF_2")
    exercise_logic = PushupLogic("Pushup")
    while cap.isOpened():
        response, frame = cap.read()
        frame = cv2.flip(frame, 1)
        exercise_logic.process_frame(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

