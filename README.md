# refactor-project
Short project to demonstrate how to refactor an existing codebase

## Problem statement 
Me: Provide me an example of working but badly written python code that accomplishes something, with the expectation that I should refactor it using SOLID principles, cohesion and decoupling, and then refactor it yourself but hide the result from me until I ask for the answer. I will use this example to train myself on analyzing bad code practices and refactoring.
ChatGPT: Certainly! Let's start with a simple example of badly written Python code. 
This code is a basic representation of a system that manages shapes (circles and rectangles) and calculates their areas. 
The code violates SOLID principles, lacks cohesion, and has tight coupling.

```
class Shape:
    def __init__(self, shape_type, radius=None, width=None, height=None):
        self.shape_type = shape_type
        self.radius = radius
        self.width = width
        self.height = height

class AreaCalculator:
    def calculate_area(self, shape):
        if shape.shape_type == 'circle':
            return 3.14 * shape.radius * shape.radius
        elif shape.shape_type == 'rectangle':
            return shape.width * shape.height
        else:
            raise ValueError("Invalid shape type")

class AreaPrinter:
    def print_area(self, shape, area):
        print(f"The area of the {shape.shape_type} is: {area}")

# Example usage
circle = Shape(shape_type='circle', radius=5)
rectangle = Shape(shape_type='rectangle', width=4, height=6)

calculator = AreaCalculator()
printer = AreaPrinter()

circle_area = calculator.calculate_area(circle)
printer.print_area(circle, circle_area)

rectangle_area = calculator.calculate_area(rectangle)
printer.print_area(rectangle, rectangle_area)

```
