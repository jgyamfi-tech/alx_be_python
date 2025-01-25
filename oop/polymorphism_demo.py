import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Raise an error to enforce implementation in derived classes."""
        raise NotImplementedError("The area method must be implemented by subclasses")


class Rectangle(Shape):
    """Derived class for rectangles."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class for circles."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)
