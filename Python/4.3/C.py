def make_equation(*args):
    if len(args) == 1:
        return str(args[0])
    return "(" + make_equation(*args[:-1]) + ") * x + " + str(args[-1])