def answer(f):
    def decotator(*args, **kwargs):
        return "Результат функции: " + str(f(*args, **kwargs))
    return decotator