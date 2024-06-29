P = 7
V = 6
P -= 3
V += 3
P += 2
V += 5
V -= 2
P += int(input())
V += int(input())
if P > V:
    print("Петя")
else:
    print("Вася")