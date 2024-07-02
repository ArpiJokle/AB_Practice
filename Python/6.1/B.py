import math
from sys import stdin

for i in stdin:
    print(math.gcd(*(map(int, i.split()))))