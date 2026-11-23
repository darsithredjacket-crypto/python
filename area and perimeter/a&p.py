import math

class circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
r=float(input("enter radius of the circle:"))
mycircle=circle(r)

print("area of cicle", mycircle.area())
print("perimeter of circle", mycircle.perimeter())