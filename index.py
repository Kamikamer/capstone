from typing import Literal
import cv2
from posture_fit_algorithm.Pushup import PushupLogic
from posture_fit_algorithm.Situp import SitupLogic
from posture_fit_algorithm.Squats import SquatsLogic
from icecream import ic
import cv2
import time
import tkinter as tk
from tkinter import Label, Button, Frame
from tkinter import messagebox
from PIL import Image, ImageTk
import math

time_previous = 0
time_current = 0
rem = 16
width, height = int(114.625*rem), int(56*rem)


def start_exercise():
    start_frame.pack_forget()
    select_exercise_frame.pack()


def select_exercise(exercise_type):
    select_exercise_frame.pack_forget()
    get_ready_frame.pack()


def get_ready():
    get_ready_frame.pack_forget()
    countdown_frame.pack()

    countdown(5)  # Start countdown from 5 seconds


def countdown(count):
    countdown_label.configure(text=str(count))
    if count > 0:
        countdown_frame.after(1000, countdown, count - 1)  # Schedule the next countdown tick after 1 second
    else:
        countdown_frame.pack_forget()
        camera_frame.pack()

        # Start the camera and show the live feed
        open_camera()


def start_camera():
    camera_frame.pack_forget()

    # Start the camera and show the live feed
    open_camera()


def open_camera():
    startTime = time.time()

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    if not cap.isOpened():
        print("Error: Failed to open camera.")
        return

    exercise_logic = PushupLogic("Pushup")  # Initialize exercise logic

    while cap.isOpened():
        response, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if not response:
            print("Error: Failed to receive frame.")
            break

        frame = cv2.flip(frame, 1)
        exercise_logic.process_frame(frame)

        captured_image = Image.fromarray(frame)
        photo_image = ImageTk.PhotoImage(image=captured_image)

        camera_label.photo = photo_image
        camera_label.configure(image=photo_image)

        camera_frame.update_idletasks()

        # Repeat the same process after every 10 milliseconds
        camera_frame.after(10, get_elapsed_time, startTime)


def get_elapsed_time(startTime):
    endTime = time.time()
    elapsedTime = endTime - startTime
    ic(elapsedTime)


app = tk.Tk()
app.geometry("1920x1080")
app.state("zoomed")

# Frames
start_frame = Frame(app)
select_exercise_frame = Frame(app)
get_ready_frame = Frame(app)
countdown_frame = Frame(app)
camera_frame = Frame(app)

# Pack the frames initially
start_frame.pack()

# Start Frame
start_button = Button(start_frame, text="Start", command=start_exercise, font=("Helvetica", 100))
start_button.pack()

# Select Exercise Frame
situps_button = Button(select_exercise_frame, text="Situps", command=lambda: select_exercise("situps"), font=("Helvetica", 100))
situps_button.pack(pady=10)
squats_button = Button(select_exercise_frame, text="Squats", command=lambda: select_exercise("squats"), font=("Helvetica", 100))
squats_button.pack(pady=10)
pushups_button = Button(select_exercise_frame, text="Pushups", command=lambda: select_exercise("pushups"), font=("Helvetica", 100))
pushups_button.pack(pady=10)

# Get Ready Frame
get_ready_label = Label(get_ready_frame, text="Get into position", font=("Helvetica", 100))
get_ready_label.pack()
get_ready_button = Button(get_ready_frame, text="Ready", command=get_ready, font=("Helvetica", 100))
get_ready_button.pack(pady=10)

# Countdown Frame
countdown_label = Label(countdown_frame, text="5", font=("Helvettica", 100))
countdown_label.pack()

# Camera Frame
camera_label = Label(camera_frame)
camera_label.pack()

app.mainloop()