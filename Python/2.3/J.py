Direction = input()

X = 0
Y = 0

while Direction != "ярно":
    Steps = int(input())
    if Direction == "яебеп":
        X += Steps
    if Direction == "чц":
        X -= Steps
    if Direction == "бнярнй":
        Y += Steps
    if Direction == "гюоюд":
        Y -= Steps
    Direction = input()
        
print(X)
print(Y)