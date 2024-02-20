import pygame
import cv2
from posture_fit_algorithm.Pushup import PushupLogic
from posture_fit_algorithm.Crunch import SitupLogic
from posture_fit_algorithm.Squats import SquatsLogic
from icecream import ic


pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Exercise App')


clock = pygame.time.Clock()


rem = 16
width, height = int(114.625*rem), int(56*rem)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


exercise_logic = None


class Button:
    def _init_(self, text, x, y, width, height, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 200, 200)
        self.text = text
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect, 2)  
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()


button_width = 200
button_height = 50


start_button = Button("Start", screen_width // 2 - button_width // 2, 300, button_width, button_height)


situps_button = Button("Situps", screen_width // 2 - button_width // 2, 400, button_width, button_height)
pushups_button = Button("Pushups", screen_width // 2 - button_width // 2, 500, button_width, button_height)
squats_button = Button("Squats", screen_width // 2 - button_width // 2, 600, button_width, button_height)


get_ready_button = Button("Get Ready", screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2, button_width, button_height)



countdown_label = Button("", screen_width // 2 - 50, screen_height // 2 + button_height, 100, 100)



state = "start"
countdown_time = 5
last_time = pygame.time.get_ticks()


running = True
while running:
    current_time = pygame.time.get_ticks()

    
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    if state == "start":
        if start_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = "exercise_selection"

        
        start_button.draw()

    elif state == "exercise_selection":
        if situps_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                exercise_logic = SitupLogic()
                state = "get_ready"
        elif pushups_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                exercise_logic = PushupLogic('Pushup')
                state = "get_ready"
        elif squats_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                exercise_logic = SquatsLogic()
                state = "get_ready"

        
        situps_button.draw()
        pushups_button.draw()
        squats_button.draw()

    elif state == "get_ready":
        if current_time - last_time > 1000:
            countdown_time -= 1
            last_time = current_time
            if countdown_time <= 0:
                state = "camera"

        
        get_ready_button.draw()

        
        countdown_label.text = str(countdown_time)
        countdown_label.draw()

    elif state == "camera":
        
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame, (0, 0))

    
    pygame.display.flip()
    clock.tick(60)


cap.release()
pygame.quit()