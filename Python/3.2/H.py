Arr = []
for i in range(int(input())):
    Arr.append(input().split())

flag = 1

Str = input()

Arr = sorted(Arr)

for i in Arr:
    if Str in i:
        print(i[0])
        flag = 0

if flag:
    print("Таких нет")