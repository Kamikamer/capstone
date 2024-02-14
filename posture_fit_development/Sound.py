import os
import time
from typing import Self
from playsound import playsound, PlaysoundException
import sys

try:
    from icecream import ic
    ic.configureOutput(includeContext=True, prefix='Booting (ツ)_/¯')
except (ImportError, ModuleNotFoundError):
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


script_dir: str | None = getattr(sys, 'MEIPASS', os.path.abspath(os.path.dirname(__file__)))
_absent = object()

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

        Returns:
            None
        """

        self.last_play_time = 0
        self.cooldown_duration = cooldown_duration

    def find_assets_directory(self) -> str | None:
        """
        Find the 'assets' directory in the directory tree.

        Returns:
            str | None: The path to the 'assets' directory if found, else None.
        """
        # Starts from the current directory
        current_dir = os.path.abspath(path=os.getcwd())
        
        # Traverses up the directory tree 
        while current_dir != "/":  
            assets_dir = os.path.join(current_dir, "assets")
            if os.path.isdir(assets_dir):
                return assets_dir
            current_dir: str = os.path.dirname(current_dir)
        
        return None   
    
    def play_sound(self, file_name=None, ignore_cd=_absent) -> None:
        """
        Plays a sound if enough time has passed since the last call.

        Args:
            file_name (str, optional): The name of the sound file to be played. Defaults to None. Passes arg to sound() method.

        Returns:
            None
        """
        epoch = time.time()

        # Check if enough time has passed since the last call
        if epoch - self.last_play_time >= self.cooldown_duration and ignore_cd is not _absent:
            self.last_play_time = epoch
            self.sound(specific_file=file_name)

        elif ignore_cd:
            self.last_play_time: float = epoch
            self.sound(specific_file=file_name)

        else:
            ic("Cooldown period active, cannot play sound yet")
            ic(ignore_cd)
            pass

    def sound(self, specific_file=_absent, ignore_cd=_absent) -> None:
        """
        Play a sound using the playsound library.

        Args:
            specific_file (str, optional): The specific sound file to play. Defaults to _absent.
            ignore_cd (bool, optional): Whether to ignore the cooldown period. Defaults to _absent.
            
        Returns:
            None
        """
        path_type = "/" if os.name == 'posix' else "\\"
        current_path: list[str] = os.getcwd().split(path_type)
        current_path[0] = "C:\\" if current_path[0] == "C:" else "/"
        
        assets_path: str | None = self.find_assets_directory()
        if assets_path is None:
            ic("Error: 'assets' folder not found.")

        if specific_file is _absent:
            playsound(sound=os.path.join(assets_path, 'note.wav'), block=ignore_cd)
        else:
            playsound(sound=os.path.join(assets_path, f"{specific_file}.wav"), block=ignore_cd)

    def sound_startup(self) -> None:
        """
        Play the startup sound.

        Returns:
            None
        """
        assets_path = self.find_assets_directory()
        if assets_path is not None:
            try:
                playsound(sound=os.path.join(assets_path, 'startup_music_cut.wav'), block=True)
            except PlaysoundException:
                ic("Error: 'startup_music_cut.wav' not found.")
            try:
                playsound(sound=os.path.join(assets_path, 'startup_greet.wav'), block=True)
            except PlaysoundException:
                ic("Error: 'startup_greet.wav' not found.")
        else:
            ic("Error: 'assets' folder not found.")
    
    def sound_booting(self) -> None:
        """
        Play the booting sound.

        Returns:
            None
        """
        assets_path: str | None = self.find_assets_directory()
        if assets_path is not None:
            try:
                playsound(sound=os.path.join(assets_path, 'booting_msg.wav'), block=False)
            except PlaysoundException:
                ic("Error: 'booting_msg.wav' not found.")
        else:
            ic("Error: 'assets' folder not found.")
            
    def sound_booting_2(self) -> None:
        """
        Play the booting sound.

        Returns:
            None
        """
        assets_path: str | None = self.find_assets_directory()
        if assets_path is not None:
            try:
                playsound(sound=os.path.join(assets_path, 'i-am-dreaming-or-final-fantasy-menu-kinda-thing-29173.wav'), block=False)
            except PlaysoundException:
                ic("Error: 'i-am-dreaming-or-final-fantasy-menu-kinda-thing-29173.wav' not found.")
        else:
            ic("Error: 'assets' folder not found.")

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