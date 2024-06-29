Cost = float(input())
Sum = 0
while Cost != 0:
    if Cost >= 500:
        Sum += Cost * 0.9
    else:
        Sum += Cost
    Cost = float(input())
print(Sum)