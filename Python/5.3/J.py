import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError (Exception):
    pass


class NeedCharError (Exception):
    pass


def password_validation(password, min_length=8, 
                        possible_chars="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM",
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    for i in password:
        if i not in possible_chars:
            raise PossibleCharError
    flag = False
    for i in password:
        if at_least_one(i):
            flag = True
    if not flag:
        raise NeedCharError
    
    return hashlib.sha256(password.encode()).hexdigest()