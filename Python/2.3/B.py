Text = input()
Answer = 0
while Text != "��������!":
    if Text.find("�����") != -1:
        Answer += 1
    Text = input()
print(Answer)