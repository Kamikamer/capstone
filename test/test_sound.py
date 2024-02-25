from posture_fit_development.Sound import SoundPlayer
import unittest


class TestSound(unittest.TestCase):
    """
    This class is a test on whether sound player works.
    Should play a sound and not the default windows sound
    """
    def test_sound(self) -> None:
        """
        Test the sound player by playing a sound.
        """
        sp = SoundPlayer()
        sp.play_sound()

    def test_sound_specific(self) -> None:
        """
        Test the specific sound functionality of the SoundPlayer class.
        """
        sp = SoundPlayer()
        sp.play_sound("IF_1")

    def test_sound_specific2(self) -> None:
        """
        Test case for playing a specific sound using the SoundPlayer class.
        """
        sp = SoundPlayer()
        sp.play_sound("IF_2")

    def test_sound_buffer(self) -> None:
        """
        Test the sound buffer functionality.
        """
        sp = SoundPlayer()
        sp.play_sound()
        sp.play_sound("IF_1")
        sp.play_sound("IF_2")
        sp.play_sound("IF_1")
        sp.play_sound("IF_2")
        sp.play_sound("IF_1")
        sp.play_sound("IF_2")
        sp.play_sound("IF_1")
        sp.play_sound("IF_2")
        sp.play_sound("IF_1")
        sp.play_sound("IF_2")
        sp.play_sound()
