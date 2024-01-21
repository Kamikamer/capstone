from posture_fit_development.Sound import SoundPlayer
import unittest


class TestSound(unittest.TestCase):
    # Should play a sound and not the default windows sound
    def test_sound(self) -> None:
        sp = SoundPlayer()
        sp.play_sound()

    def test_sound_specific(self) -> None:
        sp = SoundPlayer()
        sp.play_sound("IF_1")

    def test_sound_specific2(self) -> None:
        sp = SoundPlayer()
        sp.play_sound("IF_2")

    def test_sound_buffer(self) -> None:
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
