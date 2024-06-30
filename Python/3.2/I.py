Zoo = {}
while Str := input().split():
    for i in Str:
        if i not in Zoo:
            Zoo[i] = 1
        else:
            Zoo[i] += 1
for i in Zoo:
    print(i, Zoo[i])