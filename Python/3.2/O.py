Answer = []

for i in map(lambda x: bin(x)[2:], list(map(int, input().split()))):
    Answer.append({"digits": len(i), "units": i.count('1'), "zeros": i.count('0')})
print(Answer)