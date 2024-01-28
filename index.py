from typing import Literal
import cv2
# from posture_fit_algorithm.Detector2 import ExerciseLogic
from posture_fit_development.Sound import SoundPlayer
# from posture_fit_algorithm.Squads import SquadsLogic
# from posture_fit_development.Webcam import ExerciseLogic
import threading
from icecream import ic


time_previous = 0
time_current = 0

class Animal:
    def __init__(self, name):
        self.name = name
        self.sp = SoundPlayer()

    def speak(self):
        pass


class Dog(Animal):
    def speak(self) -> str:
        self.sp.play_sound("dog")
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        self.sp.play_sound("cat")
        return "Meow!"

if __name__ == "__main__":

    # Usage
    cat = Cat("Whiskers")
    dog = Dog("Buddy")

    print(dog.name)  
    print(dog.speak())  

    print(cat.name)  
    print(cat.speak())  
