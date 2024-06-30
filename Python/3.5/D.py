from sys import stdin

Lines = stdin.readlines()

Str = Lines[len(Lines) - 1].strip('\n')

for i in Lines[:-1]:
    if Str.lower() in i.lower():
        print(i.strip('\n'))