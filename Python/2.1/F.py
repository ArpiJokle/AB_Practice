Name = input()
Cost = int(input())
Mass = int(input())
Price = Mass * Cost
AmountOfMoney = int(input())

print("���")
print(Name, end=" - ", sep="")
print(Mass, "��", end=" - ", sep="")
print(Cost, "���/��", sep="")
print("�����: ", Price, "���", sep="")
print("�������: ", AmountOfMoney, "���", sep="")
print("�����: ", AmountOfMoney - Price, "���", sep="")