from posture_fit_development.Sound import SoundPlayer
from posture_fit_development.Webcam import CameraModule
if __name__ == "__main__":
    print("Starting app")
    sp = SoundPlayer()
    webcam = CameraModule()
    webcam.open_camera()
    sp.play_sound()