dic = {}

for i in range(int(input())):
    dic[input()] = 0

for j in range(int(input())):
    for i in range(int(input())):
        dic[input()] += 1

Arr = []

for i in dic:
    if dic[i] == 0:
        Arr.append(i)

if len(Arr) == 0:
    print("Готовить нечего")
    exit()

Arr = sorted(Arr)

for i in Arr:
    print(i)