import math

X = float(input())
Y = float(input())

if math.sqrt(X ** 2 + Y ** 2) > 10:
    print("�� ����� � ���� � �������� ���� ��������� ������!")
    exit()

if Y <= 0:
    if Y >= .25 * (X + 7) * (X - 5):
        print("���������! �������� ���� ��� ����� ������!")
        exit()
    else:
        print("���� ���������. ����������� ������.")
        exit()

if X >= 0 and X <= 5:
    if math.sqrt(X ** 2 + Y ** 2) <= 5:
        print("���������! �������� ���� ��� ����� ������!")
        exit()
    else:
        print("���� ���������. ����������� ������.")
        exit()

if X >= -7 and X <= -4:
    if Y <= (5 / 3) * X + (35 / 3):
        print("���������! �������� ���� ��� ����� ������!")
        exit()
    else:
        print("���� ���������. ����������� ������.")
        exit()

if X >= -4 and X <= 0:
    if Y <= 5:
        print("���������! �������� ���� ��� ����� ������!")
        exit()
    else:
        print("���� ���������. ����������� ������.")
        exit()

print("���� ���������. ����������� ������.")