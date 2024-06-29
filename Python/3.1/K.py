Arr = []
for i in range(int(input())):
    Arr.append(input())
Str = input()
for i in Arr:
    if (i.lower()).find(Str.lower()) != -1:
        print(i)