Text = input()
Answer = 0
while Text != "Приехали!":
    if Text.find("зайка") != -1:
        Answer += 1
    Text = input()
print(Answer)