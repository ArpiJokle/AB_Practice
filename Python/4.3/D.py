def answer(f):
    def decotator(*args, **kwargs):
        return "��������� �������: " + str(f(*args, **kwargs))
    return decotator