import json

name = input()
fin = open(name, encoding="UTF-8")
Arr = []

for i in fin:
    Arr.extend([int(x) for x in i.split()])

fin.close()

Answer = {}

Answer["count"] = len(Arr)
Answer["positive_count"] = len([x for x in Arr if x > 0])
Answer["min"] = min(Arr)
Answer["max"] = max(Arr)
Answer["sum"] = sum(Arr)
Answer["average"] = round(sum(Arr) / len(Arr), 2)

fout = open(input(), 'w', encoding="UTF-8")
json.dump(Answer, fout, ensure_ascii=False, indent=4)