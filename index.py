## Imports
### Play a melodic tune
from posture_fit_development.Startup import startup, booting, booting2, update
import threading
e = threading.Event()
e2 = threading.Event()
boot_greet = threading.Thread(target=booting, args=(e, e2))
boot_greet_2 = threading.Thread(target=booting2, args=(e2, e))

boot_greet.start()

### Alert the user that the app is starting
try:
    import pyi_splash # type: ignore
    pyi_splash.update_text("When it finishes running the background stuff, it will start the app and show the app whilst closing this app.")
except ImportError:
    pass

## Continue importing
import cv2
import json
import logging
import logging.config
import logging.handlers
import numpy as np
import os
import pathlib
import pygame
import requests
import subprocess
import sys 
from packaging import version
from posture_fit_algorithm.Pushup import PushupLogic
from posture_fit_algorithm.Crunch import CrunchLogic
from posture_fit_algorithm.Squats import SquatsLogic
from posture_fit_development.Logger import CustomLogger
from posture_fit_development.OsChecker import Statistic
from dataclasses import dataclass, field

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Reference resolution
ref_width, ref_height = 1920, 1080

# Get the current display resolution
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Calculate scaling factors
scale_x = screen_width / ref_width
scale_y = screen_height / ref_height

# Apply scaling factors
button_scale = min(scale_x, scale_y)
font_scale = min(scale_x, scale_y)
position_scale_x = screen_width / ref_width
position_scale_y = screen_height / ref_height

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Exercise App')
clock = pygame.time.Clock()

rem = 16 * button_scale
width, height = int(114.625 * rem), int(56 * rem)
state = "start"
current_logic = None
countdown_time = 5
last_time = pygame.time.get_ticks()
camera_opened = False
cap = None

# Define Button class
class Button:
    def __init__(self, text, x, y, width, height, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 200, 200)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, int(70 * font_scale))
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

# Create buttons
button_width = int(300 * button_scale)
button_height = int(200 * button_scale)

def start_action():
    global state
    state = "exercise_selection"

def crunch_action():
    global state, current_logic, camera_opened, cap, countdown_time, last_time
    current_logic = CrunchLogic("Crunch")
    state = "get_ready"
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    countdown_time = 5
    last_time = pygame.time.get_ticks()
    pygame.display.set_caption('crunches')

def pushups_action():
    global state, current_logic, camera_opened, cap, countdown_time, last_time
    current_logic = PushupLogic("Pushup")
    state = "get_ready"
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    countdown_time = 5
    last_time = pygame.time.get_ticks()
    pygame.display.set_caption('pushup')

def squats_action():
    global state, current_logic, camera_opened, cap, countdown_time, last_time
    current_logic = SquatsLogic("Squats")
    state = "get_ready"
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    countdown_time = 5
    last_time = pygame.time.get_ticks()
    pygame.display.set_caption('squats')    

def exit_action():
    global running
    running = False

start_button = Button("Start", screen_width // 2 - button_width // 2, screen_height * 0.2, button_width, button_height, action=start_action)
situps_button = Button("Crunches", screen_width // 2 - button_width // 2, screen_height * 0.4, button_width, button_height, action=crunch_action)
pushups_button = Button("Pushups", screen_width // 2 - button_width // 2, screen_height * 0.6, button_width, button_height, action=pushups_action)
squats_button = Button("Squats", screen_width // 2 - button_width // 2, screen_height * 0.8, button_width, button_height, action=squats_action)
exit_button = Button("Exit", screen_width - int(150 * position_scale_x), int(10 * position_scale_y), int(100 * position_scale_x), int(50 * position_scale_y), action=exit_action)
get_ready_button = Button("Get Ready", screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2, button_width, button_height, action=None)
countdown_label = Button("", screen_width // 2 - 50, screen_height // 2 + button_height, 100, 100, action=None)

def run_exercise_logic(exercise_logic):
    global state
    state = "get_ready"

def draw_close_text():
    font = pygame.font.Font(None, int(100 * font_scale))
    text_surface = font.render("Press q to exit or change exercise", True, BLACK)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height * 0.9))
    screen.blit(text_surface, text_rect)
    ticks = pygame.time.get_ticks()
    millis=ticks%1000
    seconds=int(ticks/1000 % 60)
    minutes=int(ticks/60000 % 24)
    out=' {minutes:02d} : {seconds:02d} : {millis} '.format(minutes=minutes, millis=millis, seconds=seconds)    
    fontt = pygame.font.Font(None, int(100 * font_scale))
    text_surf = fontt.render(f'time : {out}', True, BLACK)
    text_rectt = text_surf.get_rect(center=(screen_width // 2, int(100 * font_scale)))
    screen.blit(text_surf, text_rectt)
    fps = int(clock.get_fps())
    fonttt = pygame.font.Font(None, int(150 * font_scale))
    fpst = fonttt.render(f'fps : {fps}', True, BLACK)
    screen.blit(fpst,(int(10 * position_scale_x), int(70 * position_scale_y)))
running = True
while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in [start_button, situps_button, pushups_button, squats_button, exit_button]:
            button.handle_event(event)
    ret = False
    frame = None
    if camera_opened:
        ret, frame = cap.read()
    screen.fill(WHITE)
    if state == "start":
        start_button.draw(screen)
    elif state == "exercise_selection":
        situps_button.draw(screen)
        pushups_button.draw(screen)
        squats_button.draw(screen)
    elif state == "get_ready":
        get_ready_button.draw(screen)
        countdown_label.text = str(countdown_time)
        countdown_label.draw(screen)
        if current_time - last_time > 1000:
            countdown_time -= 1
            last_time = current_time
            if countdown_time <= 0:
                state = "exercise"
    elif state == "exercise":
        camera_opened = True
        if ret:
            # Process the logic within the frame
            if current_logic:
                current_logic.process_frame(frame)  # Assuming process_frame method handles the logic
            frame = cv2.flip(frame, 1)
            # Convert frame to RGB format for Pygame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)  # Rotate frame (adjust as needed)
            frame = pygame.surfarray.make_surface(frame)
            # Resize frame to fit Pygame display
            frame = pygame.transform.scale(frame, (screen_width, screen_height))
            # Blit frame onto Pygame display
            screen.blit(frame, (0, 0))
            draw_close_text()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        state = "exercise_selection"
                        camera_opened = False
                        # Release camera and close OpenCV windows
                        if cap is not None:
                            cap.release()
                            cv2.destroyAllWindows()
    exit_button.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

#Pushups work partially with squats
