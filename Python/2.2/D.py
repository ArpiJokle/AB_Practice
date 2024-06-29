Petya = int(input())
Vasya = int(input())
Tolya = int(input())
if Petya > Vasya and Petya > Tolya:
    print("1. Петя")
    if (Vasya > Tolya):
        print("2. Вася")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Вася")
elif (Vasya > Tolya):
    print("1. Вася")
    if Petya > Tolya:
        print("2. Петя")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Петя")
else:
    print("1. Толя")
    if Petya > Vasya:
        print("2. Петя")
        print("3. Вася")
    else:
        print("2. Вася")
        print("3. Петя")