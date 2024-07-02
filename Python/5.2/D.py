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
            return self.numer
        else:
            self.numer = data
        self.__reduce__()
    
    def denominator(self, data=None):
        if data is None:
            return self.denom
        else:
            self.denom = data
        self.__reduce__()

    def __reduce__(self):
        c = math.gcd(self.numer, self.denom)
        self.numer //= c
        self.denom //= c
    
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    
    def __repr__(self):
        return "Fraction" + str((self.numer, self.denom))