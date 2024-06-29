Name = input()
Cost = int(input())
Mass = int(input())
Price = Mass * Cost
AmountOfMoney = int(input())

print("================Чек================")

print("Товар:", end="")
print(Name.rjust(35 - 6, " "))


print("Цена:", end="")
print((str(Mass) + "кг * " + str(Cost) + "руб/кг").rjust(35 - 5))

print("Итого:", end="")
print((str(Price) + "руб").rjust(35 - 6))


print("Внесено:", end="")
print((str(AmountOfMoney) + "руб").rjust(35 - 8))

print("Сдача:", end="")
print((str(AmountOfMoney - Price) + "руб").rjust(35 - 6))

print("===================================")