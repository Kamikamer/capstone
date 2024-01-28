class Car:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        self._engine = Engine()
        self._wheel = Wheel()

    def start(self) -> None:
        self._engine.start()
        self.print_status()

    def print_status(self) -> None:
        engine_status = self._engine.status()
        wheel_status = self._wheel.status()
        print(f"Reporting status: {engine_status}, {wheel_status}")

    def drive(self) -> None:
        print(f"The {self.make} {self.model} is now moving.")
    
class Engine:
    def start(self) -> None:
        print("Engine started")

    def stop(self) -> None:
        print("Engine stopped")
    
    def status(self) -> str:
        return "OK"

class Wheel:
    def status(self) -> str:
        return "OK"

if __name__ == "__main__":
    my_car = Car(make="Toyota", model="Camry")

    my_car.start()

    my_car.drive()
