import math
List = list(map(float, input().split()))
print(math.pow(math.prod(List), 1 / len(List)))