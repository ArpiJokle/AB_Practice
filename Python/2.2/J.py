OldPass = int(input())
PartA = (OldPass % 10 + int(OldPass / 10) % 10)
PartB = (int(OldPass / 10) % 10 + int(OldPass / 100))
if PartA > PartB:
    print(PartA, PartB, sep="")
else:
    print(PartB, PartA, sep="")

