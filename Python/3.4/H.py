Arr = []
for i in range(int(input())):
    Arr.append(input())
n = int(input())
Arr *= n
for i in range(n):
    print(Arr[i])