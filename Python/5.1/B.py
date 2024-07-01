class Point:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def move(self, a, b):
        self.x += a
        self.y += b
    
    def length(self, A):
        return round(((self.x - A.x) ** 2 + (self.y - A.y) ** 2) ** 0.5, 2)