n = int(input())

Str = input()

for i in range(1, n):
    temp = input()
    if temp < Str:
        Str = temp
print(Str)