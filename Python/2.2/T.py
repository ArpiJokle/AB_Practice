Answer = ""

Str = input()
if Str.find("�����") != -1:
    Answer = Str

Str = input()
if Str.find("�����") != -1:
    if Answer == "":
        Answer = Str
    elif Str < Answer:
        Answer = Str
        
Str = input()
if Str.find("�����") != -1:
    if Answer == "":
        Answer = Str
    elif Str < Answer:
        Answer = Str

print(Answer, len(Answer), sep=" ")