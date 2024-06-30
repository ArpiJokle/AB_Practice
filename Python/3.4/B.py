First = input().split(', ')
Second = input().split(', ')

for i, j in list(zip(First, Second)):
    print(i + ' - ' + j)    