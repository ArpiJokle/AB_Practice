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

fin = open("cyrillic.txt", encoding="UTF-8")
fout = open("transliteration.txt", 'w', encoding="UTF-8")

for i in fin.read():
    if i.upper() in Code:
        if i == i.upper():
            print(Code[i], end="", file=fout)
        else:
            print(Code[i.upper()].lower(), end="", file=fout)
    else:
        print(i, end="", file=fout)

fin.close()
fout.close()