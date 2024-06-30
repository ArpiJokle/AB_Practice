dic = {}
for i in range(int(input())):
    Str = input()
    if Str in dic:
        dic[Str] += 1
    else:
        dic[Str] = int(1)

Arr = []

for i in dic:
    if dic[i] != 1:
        Arr.append(i + " - " + str(dic[i]))

Arr = sorted(Arr)

if len(Arr) == 0:
    print("Однофамильцев нет")
    exit()

for i in Arr:
    print(i)