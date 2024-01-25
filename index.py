from posture_fit_development.Sound import SoundPlayer
from posture_fit_development.Webcam import CameraModule
import threading

time_previous = 0
time_current = 0

if __name__ == "__main__":
    print("Starting app")
    sp = SoundPlayer()
    sp.play_sound()
    webcam = CameraModule()
    webcam.open_camera()