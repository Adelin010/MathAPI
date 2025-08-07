from abc import ABC, abstractmethod
import math

type Numeric = int | float


class Shape(ABC):

    @abstractmethod
    def area(self) -> Numeric:
        pass 


class Rectangle (Shape):

    """
    A class representing a rectangle, inheriting from the abstract class `Shape`.

    This class models a rectangle with a given width and height and provides a
    concrete implementation for calculating its area.

    Attributes:
        width (Numeric): The width of the rectangle.
        height (Numeric): The height of the rectangle.
    """

    def __init__(self, width: Numeric, height: Numeric):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __str__(self) -> str:
        return f"RSectangle with widht {self.width} and height {self.height}"


class Circle(Shape):
    """ A class representing a circle, inheriting from the abstract class `Shape`.

    This class models a circle with a given radius and provides a concrete
    implementation for calculating its area.

    Attributes:
        radius (Numeric): The radius of the circle.
    """

    def __init__(self, radius: Numeric):
        self.radius = radius

    def area(self):
        return (self.radius**2) * math.pi
    
    def __str__(self) -> str:
        return f"Circle with radius {self.radius}"
    