class Rectangle:
    def __init__(self, a, b):
        self.xleft = round(min(a[0], b[0]), 2)
        self.xright = round(max(a[0], b[0]), 2)
        self.ytop = round(max(a[1], b[1]), 2)
        self.ybot = round(min(a[1], b[1]), 2)
        self.width = round(abs(self.xleft - self.xright), 2)
        self.length = round(abs(self.ytop - self.ybot), 2)
    
    def perimeter(self):
        return round(2 * (self.length + self.width), 2)
    
    def area(self):
        return round(self.width * self.length, 2)