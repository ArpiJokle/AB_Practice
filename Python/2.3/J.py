Direction = input()

X = 0
Y = 0

while Direction != "����":
    Steps = int(input())
    if Direction == "�����":
        X += Steps
    if Direction == "��":
        X -= Steps
    if Direction == "������":
        Y += Steps
    if Direction == "�����":
        Y -= Steps
    Direction = input()
        
print(X)
print(Y)