try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa
    
class Car:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        self._engine = Engine()
        self._wheel = Wheel()

    def start(self) -> None:
        self._engine.start()
        self.status_menu()

    def status_menu(self) -> None:
        engine_status = self._engine.status()
        wheel_status = self._wheel.status()
        ic(f"Reporting status: {engine_status}, {wheel_status}")

    def drive(self) -> None:
        ic(f"The {self.make} {self.model} is now moving.")
    
class Engine:
    def start(self) -> None:
        ic("Engine started")

    def stop(self) -> None:
        ic("Engine stopped")
    
    def status(self) -> str:
        return "OK"

class Wheel:
    def status(self) -> str:
        return "OK"

if __name__ == "__main__":
    my_car = Car(make="Toyota", model="Camry")

    my_car.start()

    my_car.drive()
