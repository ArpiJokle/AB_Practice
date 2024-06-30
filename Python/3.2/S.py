Items = []

for i in range(int(input())):
    Items.extend(set(list(map(lambda x: x.strip(','), input().split()))[1:]))

Items = sorted(Items)

for i in Items:
    if Items.count(i) == 1:
        print(i)