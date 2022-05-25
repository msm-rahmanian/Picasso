from shape import Shape
import math


class Circle(Shape):

    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area
