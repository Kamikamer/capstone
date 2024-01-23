import os
import time
from playsound import playsound

class SoundPlayer:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SoundPlayer, cls).__new__(cls)
        return cls.instance

    def __init__(self, cooldown_duration=3) -> None:
        self.last_play_time = 0
        self.cooldown_duration = cooldown_duration
        
    def play_sound(self, file_name=None) -> None:
        current_time = time.time()
        print(f"Epoch: {current_time}")
        # Check if enough time has passed since the last call
        if current_time - self.last_play_time >= self.cooldown_duration:
            # Update the last play time
            self.last_play_time = current_time
            # Play the sound
            self.sound(file_name)
        else:
            print("Cooldown period active, cannot play sound yet")
            
    def sound(self, specific_file=None) -> None:
        print('Playing sound using playsound lib')
        path_type = "/" if os.name == 'posix' else "\\"

        # Pathing
        current_path = os.getcwd().split(path_type)
        print(f"Current path: {current_path}")
        current_path[0] = "C:\\" if current_path[0] == "C:" else "/"
        if current_path[-1] == 'posture_fit_development':
            current_path = os.path.join(*current_path[:-1], 'assets')
        elif current_path[-1] == 'posture_fit_algorithm':
            current_path = os.path.join(*current_path[:-1], 'assets')
        elif current_path[-1] == 'capstone':
            current_path = os.path.join(*current_path, "assets")
        else:
            current_path = os.path.join(*current_path)
        # Play the sound
        if specific_file is None:
            playsound(os.path.join(current_path + rf'{path_type}note.wav'))
        else:
            playsound(os.path.join(current_path + rf'{path_type}{specific_file}.wav'))

if __name__ == '__main__':
    sp = SoundPlayer()
    sp2 = SoundPlayer()
    sp.play_sound()
    sp.play_sound("IF_1") 
    sp.play_sound("IF_2")
    sp2.play_sound("IF_1")
    sp.play_sound("IF_2")
    sp.play_sound("IF_1")
    sp2.play_sound("IF_2")
    sp.play_sound("IF_1")
    sp.play_sound("IF_2")
    sp2.play_sound("IF_1")
    sp.play_sound("IF_2")
    sp2.play_sound()