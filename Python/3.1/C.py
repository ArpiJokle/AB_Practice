Len = int(input())

n = int(input())

for i in range(0, n):
    Str = input()
    print(Str[:Len - 3] + "..." if len(Str) > Len else Str)