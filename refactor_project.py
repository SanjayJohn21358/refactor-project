from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def print_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def print_area(self):
        print(f"The area of the rectangle is: {self.calculate_area()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius**2)
    
    def print_area(self):
        print(f"The area of the circle is: {self.calculate_area()}")


# Example usage
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

circle.print_area()
rectangle.print_area()


