from posture_fit_development.Sound import SoundPlayer
from posture_fit_development.Webcam import CameraModule
import cv2
time_previous = 0
time_current = 0
cap = cv2.VideoCapture(0)
if __name__ == "__main__":
    print("Starting app")
    sp = SoundPlayer()
    webcam = CameraModule()
    webcam.open_camera()
    sp.play_sound()