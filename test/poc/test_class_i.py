from posture_fit_development.Sound import SoundPlayer

class Animal():
    name_cls = "Animal"

    def __init__(self, name, sound_type) -> None:
        self.name = name
        self._setup_sound_player(sound_type=sound_type)

    def _setup_sound_player(self, sound_type) -> None:
        self.sp = SoundPlayer()
        self.sound_type = sound_type

    def speak(self) -> str:
        self.sp.play_sound(self.sound_type)
        print(f"Self.name {self.name}")
        return "Generic animal sound"
    
    def print_name(self) -> str:
        return self.name


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, sound_type="dog")

    def speak(self) -> str:
        super().speak()
        return "Woof!"


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, sound_type="cat")

    def speak(self) -> str:
        super().speak()
        return "Meow!"

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(dog.name)  
    print(dog.speak())  
    print(dog.print_name())

    print(cat.name)  
    print(cat.speak())  
    print(cat.print_name())