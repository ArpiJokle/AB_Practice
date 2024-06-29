List = ("Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая")
k = 0
for i in range(int(input())):
    print(List[k])
    k += 1
    if k > 4:
        k = 0