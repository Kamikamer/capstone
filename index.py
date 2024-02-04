from typing import Literal
import cv2
from posture_fit_algorithm.Pushup import PushupLogic
from posture_fit_algorithm.Situp import SitupLogic
from icecream import ic
import cv2
import time
import tkinter as tk
from tkinter import Label, Button
from tkinter import messagebox
from PIL import Image, ImageTk


time_previous = 0
time_current = 0
rem = 16
width, height = 114.625*rem, 56*rem


def open_camera():
    startTime = time.time()

    # Capture the video frame by frame
    response, frame = cap.read()

    # Convert image from one color space to other
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    exercise_logic = PushupLogic("Pushup")
    exercise_logic.process_frame(opencv_image)

    # Capture the latest frame and transform to image
    captured_image = Image.fromarray(opencv_image)

    # Convert captured image to photoimage
    photo_image = ImageTk.PhotoImage(image=captured_image)

    # Displaying photoimage in the label
    label_widget.photo_image = photo_image

    # Configure image in the label
    label_widget.configure(image=photo_image)

    # Repeat the same process after every 10 miliseconds
    label_widget.after(10, open_camera)
    get_elapsed_time(startTime)


def get_elapsed_time(startTime):
    endTime = time.time()

    elapsedTime = endTime - startTime
    ic(elapsedTime)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

app = tk.Tk()
app.geometry("1920x1080")
app.state("zoomed")

app.bind('<Escape>', lambda e: app.quit())


label_widget = Label(app, width=width, height=height)
label_widget.pack(padx=2.6 * rem, pady=2.6 * rem)

button1 = Button(app, text="Open Camera",
                 command=open_camera)
button1.pack()

app.mainloop()

