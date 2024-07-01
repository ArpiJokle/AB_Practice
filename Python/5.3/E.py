def merge(a, b):
    try:
        iter(a)
        iter(b)
    except TypeError:
        raise StopIteration
    
    flag1 = all(isinstance(i, type(a[0])) for i in a)
    flag2 = all(isinstance(i, type(b[0])) for i in a)
    if not (flag1 and flag2):
        raise TypeError

    if list(a) != sorted(a) or list(b) != sorted(b):
        raise ValueError
    return tuple(sorted(list(a) + list(b)))