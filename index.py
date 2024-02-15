## Imports
### Play a melodic tune
from posture_fit_development.Startup import startup, booting, booting2
import threading
e = threading.Event()
e2 = threading.Event()
boot_greet = threading.Thread(target=booting, args=(e, e2))
boot_greet_2 = threading.Thread(target=booting2, args=(e2, e))

boot_greet.start()
# boot_greet_2.start() 

### Alert the user that the app is starting
try:
    import pyi_splash # type: ignore
    pyi_splash.update_text("When it finishes running the background stuff, it will start the app and show the app whilst closing this app.")
except ImportError:
    pass
## Continue importing
import pygame
import cv2
import numpy as np
from posture_fit_algorithm.Pushup import PushupLogic
from posture_fit_algorithm.Situp import SitupLogic
from posture_fit_algorithm.Squats import SquatsLogic

try:
    pyi_splash.close()
except NameError:
    pass

## Initializers


app_thread = threading.Thread(target=pygame.init)

# Start both threads
app_thread.start()
greeting = threading.Thread(target=startup)
greeting.start()

## Constants

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_width = 760
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Exercise App')

clock = pygame.time.Clock()

rem = 16
width, height = int(114.625*rem), int(56*rem)

# Initialize VideoCapture with cv2.CAP_DSHOW flag

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

state = "start"
current_logic = None
countdown_time = 5
last_time = pygame.time.get_ticks()

## Classes and functions

def run_exercise_logic(exercise_logic) -> None:
    global state, current_logic
    current_logic = exercise_logic
    state = "get_ready"
    
def change_to_exercise_selection() -> None:
    global state
    state = "exercise_selection"

### Buttons

class Button:
    def __init__(self, text, x, y, width, height, action) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 200, 200)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

button_width = 200
button_height = 50

start_button = Button("Start", screen_width // 2 - button_width // 2, 300, button_width, button_height, action=None)

situps_button = Button("Situps", screen_width // 2 - button_width // 2, 400, button_width, button_height, action=None)
pushups_button = Button("Pushups", screen_width // 2 - button_width // 2, 500, button_width, button_height, action=None)
squats_button = Button("Squats", screen_width // 2 - button_width // 2, 600, button_width, button_height, action=None)

get_ready_button = Button("Get Ready", screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2, button_width, button_height, action=None)

countdown_label = Button("", screen_width // 2 - 50, screen_height // 2 + button_height, 100, 100, action=None)


## Running code
running = True
while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Read frame from OpenCV capture
    ret, frame = cap.read()
    screen.fill(WHITE)

    if state == "start":
        start_button.draw(screen)
        if start_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = "exercise_selection"


    elif state == "exercise_selection":
        situps_button.draw(screen)
        pushups_button.draw(screen)
        squats_button.draw(screen)

        if situps_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                run_exercise_logic(SitupLogic("Situp"))
        elif pushups_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                run_exercise_logic(PushupLogic("Pushup"))
        elif squats_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                run_exercise_logic(SquatsLogic("Squats"))

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

            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                state = "exercise_selection"
                # Release camera and close OpenCV windows
                cap.release()
                cv2.destroyAllWindows()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
