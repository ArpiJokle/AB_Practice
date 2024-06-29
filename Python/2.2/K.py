c = int(input())

a = c % 10
c = int(c / 10)

b = c % 10
c = int(c / 10)

Max = 0
Min = 0
Other = 0

if a >= b and a >= c:
    Max = a
    Min = b
    Other = c
    if b >= c:
        Min = c
        Other = b
if b >= a and b >= c:
    Max = b
    Min = a
    Other = c
    if a >= c:
        Min = c
        Other = a
if c >= b and c >= a:
    Max = c
    Min = a
    Other = b
    if a >= b:
        Min = b
        Other = a

if Max + Min == Other * 2:
    print("YES")
else:
    print("NO")