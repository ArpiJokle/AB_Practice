N = int(input())
M = int(input())
First = []
for i in range(N):
    First.append(input())
Second = []
for i in range(M):
    Second.append(input())
Both = set(First) & set(Second)
print("Таких нет" if len(Both) == 0 else len(Both))