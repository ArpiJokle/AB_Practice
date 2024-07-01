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