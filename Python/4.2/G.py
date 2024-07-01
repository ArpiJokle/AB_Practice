Data = list()


def enter_results(*args):
    global Data
    if isinstance(args, int):
        Data += args
    else:
        Data += list(args)


def get_sum():
    return (sum(Data[::2]), sum(Data[1::2]))


def get_average():
    Sum = get_sum()
    return (round(2 * Sum[0] / len(Data), 2), 
            round(2 * Sum[1] / len(Data), 2))