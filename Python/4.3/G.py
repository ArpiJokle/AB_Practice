def same_type(f):
    def decotator(*args):
        if len(set([type(i) for i in args])) == 1:
            return f(*args)
        else:
            print("���������� ��������� ���� ������")
            return False
    return decotator