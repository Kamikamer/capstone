import os
import time
from typing import Self
from playsound import playsound
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

class SoundPlayer:
    def __new__(cls) -> Self:
        """
        Create a new instance of the SoundPlayer class if it doesn't already exist.
        
        Returns:
            Self: The instance of the SoundPlayer class. If it already exists, return the existing instance (Singleton concept).
        """
        if not hasattr(cls, 'instance'):
            cls.instance: Self = super(SoundPlayer, cls).__new__(cls)
        return cls.instance
        
    def __init__(self, cooldown_duration=3) -> None:
        """
        Initialize the Sound object.

        Args:
            cooldown_duration (int, optional): The cooldown duration in seconds. Defaults to 3.
        """

        self.last_play_time = 0
        self.cooldown_duration = cooldown_duration
        
    def play_sound(self, file_name=None) -> None:
        """
        Plays a sound if enough time has passed since the last call.

        Args:
            file_name (str, optional): The name of the sound file to be played. Defaults to None. Passes arg to sound() method.
        """
        epoch = time.time()
        # print("=============== Sound ===============")
        # ic(datetime.fromtimestamp(epoch).strftime('%H:%M:%S'))  # type: ignore
        # Check if enough time has passed since the last call
        if epoch - self.last_play_time >= self.cooldown_duration:
            # Update the last play time
            self.last_play_time = epoch
            # Play the sound
            self.sound(file_name)
        else:
            # ic("Cooldown period active, cannot play sound yet")
            pass
        # print("=====================================")

    def sound(self, specific_file=None) -> None:
        """
        Play a sound using the playsound library.

        Args:
            specific_file (str, optional): The specific sound file to play. Defaults to None.
        """
        ic('Playing sound using playsound lib')
        path_type = "/" if os.name == 'posix' else "\\"
        current_path = os.getcwd().split(path_type)
        current_path[0] = "C:\\" if current_path[0] == "C:" else "/"

        if current_path[-1] == 'posture_fit_development':
            current_path = os.path.join(*current_path[:-1], 'assets')
        elif current_path[-1] == 'posture_fit_algorithm':
            current_path = os.path.join(*current_path[:-1], 'assets')
        elif current_path[-1] == 'capstone':
            current_path = os.path.join(*current_path, "assets")
        else:
            current_path = os.path.join(*current_path)

        if specific_file is None:
            playsound(os.path.join(current_path + rf'{path_type}note.wav'))
        else:
            playsound(os.path.join(current_path + rf'{path_type}{specific_file}.wav'))

if __name__ == '__main__':
    ic.configureOutput(prefix='Sound System (ツ)_/¯ ')
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
