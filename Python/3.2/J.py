Code = {
    'À': 'A', 'Á': 'B', 'Â': 'V',
    'Ã': 'G', 'Ä': 'D', 'Å': 'E',
    '¨': 'E', 'Æ': 'Zh', 'Ç': 'Z',
    'È': 'I', 'É': 'I', 'Ê': 'K',
    'Ë': 'L', 'Ì': 'M', 'Í': 'N',
    'Î': 'O', 'Ï': 'P', 'Ð': 'R',
    'Ñ': 'S', 'Ò': 'T', 'Ó': 'U',
    'Ô': 'F', 'Õ': 'Kh', 'Ö': 'Tc',
    '×': 'Ch', 'Ø': 'Sh', 'Ù': 'Shch',
    'Û': 'Y', 'Ý': 'E', 'Þ': 'Iu',
    'ß': 'Ia', 'Ü': '', 'Ú': '',
}

for i in input():
    if i.upper() in Code:
        if i == i.upper():
            print(Code[i], end="")
        else:
            print(Code[i.upper()].lower(), end="")
    else:
        print(i, end="")