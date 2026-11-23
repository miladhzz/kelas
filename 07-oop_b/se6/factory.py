from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def name(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def name(self):
        return "دایره"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def name(self):
        return "مربع"


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def name(self):
        return "مثلث"


# --- کارخانه ---
class ShapeFactory:
    @staticmethod
    def create(shape_type, **kwargs):
        if shape_type == "circle":
            return Circle(**kwargs)
        elif shape_type == "square":
            return Square(**kwargs)
        elif shape_type == "triangle":
            return Triangle(**kwargs)
        raise ValueError(f"نوع شکل ناشناخته: {shape_type}")


# استفاده
shapes = [
    ShapeFactory.create("circle", radius=3),
    ShapeFactory.create("square", side=4),
    ShapeFactory.create("triangle", base=5, height=2),
]

for s in shapes:
    print(f"{s.name()}: مساحت = {s.area():.2f}")