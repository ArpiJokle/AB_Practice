Name = input()
Cost = int(input())
Mass = int(input())
Price = Mass * Cost
AmountOfMoney = int(input())

print("================���================")

print("�����:", end="")
print(Name.rjust(35 - 6, " "))


print("����:", end="")
print((str(Mass) + "�� * " + str(Cost) + "���/��").rjust(35 - 5))

print("�����:", end="")
print((str(Price) + "���").rjust(35 - 6))


print("�������:", end="")
print((str(AmountOfMoney) + "���").rjust(35 - 8))

print("�����:", end="")
print((str(AmountOfMoney - Price) + "���").rjust(35 - 6))

print("===================================")