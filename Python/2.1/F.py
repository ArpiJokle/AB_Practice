Name = input()
Cost = int(input())
Mass = int(input())
Price = Mass * Cost
AmountOfMoney = int(input())

print("Чек")
print(Name, end=" - ", sep="")
print(Mass, "кг", end=" - ", sep="")
print(Cost, "руб/кг", sep="")
print("Итого: ", Price, "руб", sep="")
print("Внесено: ", AmountOfMoney, "руб", sep="")
print("Сдача: ", AmountOfMoney - Price, "руб", sep="")