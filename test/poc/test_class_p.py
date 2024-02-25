class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == "__main__":
    # Function that calculates the area of a shape
    def calculate_area(shape):
        return shape.area()

    # Creating instances of different shapes
    circle = Circle(radius=5)
    square = Square(side_length=4)
    triangle = Triangle(base=3, height=6)

    # Using polymorphism with the function
    print(f"Area of Circle: {calculate_area(circle)}")
    print(f"Area of Square: {calculate_area(square)}")
    print(f"Area of Triangle: {calculate_area(triangle)}")
