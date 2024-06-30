fin = open(input(), encoding="UTF-8")
Arr = []
for i in fin:
    Arr.append(i)
for i in Arr[-int(input()):]:
    print(i.strip())