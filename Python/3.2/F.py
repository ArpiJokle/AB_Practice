N = int(input())
M = int(input())
Arr = []
for i in range(N + M):
    Arr.append(input())
Arr = sorted(Arr)
Answer = []
for i in Arr:
    if Arr.count(i) == 1:
        Answer.append(i)

Answer = sorted(Answer)

print("\n".join(Answer) if len(Answer) != 0 else "Таких нет")