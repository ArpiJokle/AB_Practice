fin = open(input(), encoding="UTF-8")
Arr1 = []
for i in fin:
    Arr1.extend(i.strip().split())
fin.close()
fin = open(input(), encoding="UTF-8")
Arr2 = []
for i in fin:
    Arr2.extend(i.strip().split())
fin.close()
fin = open(input(), 'w', encoding="UTF-8")
for i in sorted(list(set(Arr1) ^ set(Arr2))):
    print(i, file=fin)