class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        print("Getting width")
        return self._width

    @width.setter
    def width(self, value):
        print("Setting width")
        if value >= 0:
            self._width = value
        else:
            raise ValueError("Width must be non-negative")

    @property
    def height(self):
        print("Getting height")
        return self._height

    @height.setter
    def height(self, value):
        print("Setting height")
        if value >= 0:
            self._height = value
        else:
            raise ValueError("Height must be non-negative")

    @property
    def area(self):
        print("Calculating area")
        return self._width * self._height

if __name__ == "__main__":
    rectangle = Rectangle(width=5, height=3)

    # Accessing attributes using properties
    print("Width:", rectangle.width)
    print("Height:", rectangle.height)

    # Setting attributes using properties
    rectangle.width = 7
    rectangle.height = 4

    # Accessing the area property
    print("Area:", rectangle.area)
