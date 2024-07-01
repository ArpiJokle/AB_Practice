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


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    for i in name:
        if i.lower() not in "יצףךוםדרשחץתפûגאןנמכהז‎ÿקסלטעüב‏¸":
            raise CyrillicError
    if name != name.lower().capitalize():
        raise CapitalError
    return name


def user_validation(**args):
    if len(args) != 3:
        raise KeyError
    for i in args:
        if i not in ["last_name", "first_name", "username"]:
            raise KeyError
    for i in args.values():
        if not isinstance(i, str):
            raise TypeError
    name_validation(args["last_name"])
    name_validation(args["first_name"])
    username_validation(args["username"])
    return args