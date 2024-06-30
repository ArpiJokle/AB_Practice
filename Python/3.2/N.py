Items = []

for i in range(int(input())):
    Items.append(input())

Food = []

for k in range(int(input())):
    Name = input()
    flag = 1
    for i in range(int(input())):
        if input() not in Items:
            flag = 0
    if flag:
        Food.append(Name)

if len(Food) == 0:
    print("Готовить нечего")
    exit()

Food = sorted(Food)

for i in Food:
    print(i)