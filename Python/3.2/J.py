Code = {
    '�': 'A', '�': 'B', '�': 'V',
    '�': 'G', '�': 'D', '�': 'E',
    '�': 'E', '�': 'Zh', '�': 'Z',
    '�': 'I', '�': 'I', '�': 'K',
    '�': 'L', '�': 'M', '�': 'N',
    '�': 'O', '�': 'P', '�': 'R',
    '�': 'S', '�': 'T', '�': 'U',
    '�': 'F', '�': 'Kh', '�': 'Tc',
    '�': 'Ch', '�': 'Sh', '�': 'Shch',
    '�': 'Y', '�': 'E', '�': 'Iu',
    '�': 'Ia', '�': '', '�': '',
}

for i in input():
    if i.upper() in Code:
        if i == i.upper():
            print(Code[i], end="")
        else:
            print(Code[i.upper()].lower(), end="")
    else:
        print(i, end="")