Str = input()

for i in Str:
    if int(i) % 2 == 0:
        continue
    print(i, end="")