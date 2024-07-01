class Point:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def move(self, a, b):
        self.x += a
        self.y += b
    
    def length(self, A):
        return round(((self.x - A.x) ** 2 + (self.y - A.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if not args:
            self.x = 0
            self.y = 0
        elif len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
        else:
            self.x = args[0]
            self.y = args[1]
    
    def __str__(self):
        return str((self.x, self.y))
    
    def __repr__(self):
        return "PatchedPoint" + self.__str__()