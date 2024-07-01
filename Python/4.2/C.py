def GCD(a, b):
    while a != b:
        if a > b:   
            a -= b
        else:
            b -= a
    return a


def gcd(*args):
    if isinstance(args, int):
        return args[0]
    a = args[0]
    for i in args[1:]:
        a = GCD(a, i)
    return a