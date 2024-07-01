class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError
    if not (isinstance(b, float) or isinstance(b, int)):
        raise TypeError
    if not (isinstance(c, float) or isinstance(c, int)):
        raise TypeError
    if a == 0:
        if b == 0:
            if c == 0:
                raise InfiniteSolutionsError
            else:
                raise NoSolutionsError 
        return (-(c / b))
    if a != 0 and b == c and b == 0:
        return (0, 0)
    D = b ** 2 - (4 * a * c)
    if D < 0:
        raise NoSolutionsError 
    if D == 0:
        return (-1 * b) / (2 * a), (-1 * b) / (2 * a)
    A = (-1 * b - (D ** 0.5)) / (2 * a)
    B = (-1 * b + (D ** 0.5)) / (2 * a)
    if A < B:
        return A, B
    return B, A