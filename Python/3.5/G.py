name = input()
fin = open(name, encoding="UTF-8")
Arr = []

for i in fin:
    Arr.extend([int(x) for x in i.split()])

fin.close()

print(len(Arr))
print(len([x for x in Arr if x > 0]))
print(min(Arr))
print(max(Arr))
print(sum(Arr))
print(f'{sum(Arr) / len(Arr):.3}')