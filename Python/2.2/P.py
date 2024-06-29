Petya = int(input())
Vasya = int(input())
Tolya = int(input())
if Petya > Vasya and Petya > Tolya:
    print("Петя".rjust(14))
    if (Vasya > Tolya):
        print("Вася".rjust(6))
        print("Толя".rjust(22))
    else:
        print("Толя".rjust(6))
        print("Вася".rjust(22))
elif (Vasya > Tolya):
    print("Вася".rjust(14))
    if Petya > Tolya:
        print("Петя".rjust(6))
        print("Толя".rjust(22))
    else:
        print("Толя".rjust(6))
        print("Петя".rjust(22))
else:
    print("Толя".rjust(14))
    if Petya > Vasya:
        print("Петя".rjust(6))
        print("Вася".rjust(22))
    else:
        print("Вася".rjust(6))
        print("Петя".rjust(22))

print("   II      I      III   ")