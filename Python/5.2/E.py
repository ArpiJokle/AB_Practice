import math


class Fraction:
    def __init__(self, *data):
        if isinstance(data[0], str):
            self.numer, self.denom = map(int, data[0].split('/'))
        else:
            self.numer, self.denom = data[0], data[1]
        self.__reduce__()

    def numerator(self, data=None):
        if data is None:
            return abs(self.numer)
        else:
            temp = self.numer // abs(self.numer)
            self.numer = data * temp
        self.__reduce__()
    
    def denominator(self, data=None):
        if data is None:
            return abs(self.denom)
        else:
            temp = self.denom // abs(self.denom)
            self.denom = data * temp
        self.__reduce__()

    def __reduce__(self):
        if self.denom < 0:
            self.denom *= -1
            self.numer *= -1
        c = math.gcd(self.numer, self.denom)
        self.numer //= c
        self.denom //= c
    
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    
    def __repr__(self):
        return "Fraction('" + self.__str__() + "')"
    
    def __neg__(self):
        return Fraction(-1 * self.numer, self.denom)