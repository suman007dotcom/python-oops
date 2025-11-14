import math

class shape:
    def area(self):
        return 0
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
class rectangle(shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return math.pi * self.a * self.b

shapes = [
    circle(5),
    rectangle(4, 6)
]
for Shape in shapes:
    print(f"{Shape.__class__.__name__} Area: {Shape.area():.2f}")
