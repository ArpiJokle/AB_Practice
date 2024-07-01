class BadCharacterError (Exception):
    pass


class StartsWithDigitError (Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    for i in name:
        if i.lower() not in "1234567890_qwertyuiopasdfghjklzxcvbnm":
            raise BadCharacterError
    if name[0] in "1234567890":
        raise StartsWithDigitError
    return name