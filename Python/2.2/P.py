Petya = int(input())
Vasya = int(input())
Tolya = int(input())
if Petya > Vasya and Petya > Tolya:
    print("����".rjust(14))
    if (Vasya > Tolya):
        print("����".rjust(6))
        print("����".rjust(22))
    else:
        print("����".rjust(6))
        print("����".rjust(22))
elif (Vasya > Tolya):
    print("����".rjust(14))
    if Petya > Tolya:
        print("����".rjust(6))
        print("����".rjust(22))
    else:
        print("����".rjust(6))
        print("����".rjust(22))
else:
    print("����".rjust(14))
    if Petya > Vasya:
        print("����".rjust(6))
        print("����".rjust(22))
    else:
        print("����".rjust(6))
        print("����".rjust(22))

print("   II      I      III   ")