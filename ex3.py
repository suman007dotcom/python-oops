class circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"area of the circle with radius {self.radius} is {3.14*(self.radius**2)}")
    def perimeter(self):
        print(f"perimeter of the circle with radius {self.radius} is {2*3.14*self.radius}")
circle1 = circle(2)
circle1.area()
circle1.perimeter()