fin = open(input(), encoding="UTF-8")
Arr = []
for i in fin:
    Arr.append(i.strip().replace('\t', '').split())
fin.close()
fout = open(input(), 'w', encoding="UTF-8")
for i in Arr:
    if any(i):
        print(' '.join(i), file=fout)
fout.close()