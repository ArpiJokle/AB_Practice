n = int(input())

flag = 0

for i in range(0, n):
    First = input()[0]
    if First != 'à' and First != 'á' and First != 'â':
        flag = 1

print("NO" if flag else "YES")