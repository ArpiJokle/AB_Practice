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
    
    def __add__(self, other):
        return Fraction(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)
    
    def __iadd__(self, other):
        self.numer, self.denom = self.numer * other.denom + self.denom * other.numer, self.denom * other.denom
        self.__reduce__()
        return self
    
    def __sub__(self, other):
        return Fraction(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)
    
    def __isub__(self, other):
        self.numer, self.denom = self.numer * other.denom - self.denom * other.numer, self.denom * other.denom
        self.__reduce__()
        return self
    
    def __mul__(self, other):
        return Fraction(self.numer * other.numer, self.denom * other.denom)
    
    def __imul__(self, other):
        self.numer, self.denom = self.numer * other.numer, self.denom * other.denom
        self.__reduce__()
        return self
    
    def __truediv__(self, other):
        return Fraction(self.numer * other.denom, self.denom * other.numer)
    
    def __itruediv__(self, other):
        self.numer, self.denom = self.numer * other.denom, self.denom * other.numer
        self.__reduce__()
        return self
    
    def reverse(self):
        return Fraction(self.denom, self.numer)
    
    def __lt__(self, other):
        return self.numer / self.denom < other.numer / other.denom
    
    def __le__(self, other):
        return self.numer / self.denom <= other.numer / other.denom
    
    def __gt__(self, other):
        return self.numer / self.denom > other.numer / other.denom
    
    def __ge__(self, other):
        return self.numer / self.denom >= other.numer / other.denom
    
    def __eq__(self, other):
        return self.numer / self.denom == other.numer / other.denom
    
    def __ne__(self, other):
        return self.numer / self.denom != other.numer / other.denom