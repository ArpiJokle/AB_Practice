Petya = int(input())
Vasya = int(input())
Tolya = int(input())
if Petya > Vasya and Petya > Tolya:
    print("1. ����")
    if (Vasya > Tolya):
        print("2. ����")
        print("3. ����")
    else:
        print("2. ����")
        print("3. ����")
elif (Vasya > Tolya):
    print("1. ����")
    if Petya > Tolya:
        print("2. ����")
        print("3. ����")
    else:
        print("2. ����")
        print("3. ����")
else:
    print("1. ����")
    if Petya > Vasya:
        print("2. ����")
        print("3. ����")
    else:
        print("2. ����")
        print("3. ����")