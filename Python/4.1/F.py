Lines = []


def modern_print(Str):
    if Str not in Lines:
        print(Str)
        Lines.append(Str)