dic = {}
for i in range(int(input())):
    Str = input()
    if Str in dic:
        dic[Str] += 1
    else:
        dic[Str] = int(1)

Count = 0

for i in dic:
    if dic[i] != 1:
        Count += int(dic[i])

print(Count)