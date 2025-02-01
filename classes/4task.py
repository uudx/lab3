import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x0 = 0
        self.y0 = 0
    
    def show(self):
        print(f"x: {self.x}")
        print(f"y: {self.y}")
    
    def move(self):
        self.x0 = self.x
        self.y0 = self.y
        self.x = int(input("new x: "))
        self.y = int(input("new y: "))
    
    def dist(self):
        print(f"distance between old and new coordinates = {math.sqrt((self.x-self.x0)**2 + (self.y-self.y0)**2)}")
    
point = Point(100,200)
point.show()
point.move()
point.show()
point.dist()
