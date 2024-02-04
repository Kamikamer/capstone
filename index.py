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
from tkinter import Label, Button
from tkinter import messagebox
from PIL import Image, ImageTk 


def open_camera() -> None: 
    _, frame = cap.read() 
    captured_image = Image.fromarray(opencv_image) 
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    photo_image = ImageTk.PhotoImage(image=captured_image) 
    label_widget.configure(image=photo_image) 
    label_widget.after(10, open_camera) 


time_previous = 0
time_current = 0
rem = 16
width, height = 114*rem, 56*rem 


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 

app = tk.Tk() 
app.geometry("1920x1080")
app.bind('<Escape>', lambda e: app.quit()) 
label_widget = Label(app) 
label_widget.pack() 

button1 = Button(app, text="Open Camera", 
                 command=open_camera) 
button1.pack() 

app.mainloop() 