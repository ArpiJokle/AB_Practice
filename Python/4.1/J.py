def merge(first, second):
    Arr = list(first) + list(second)
    for i in range(len(Arr)):
        for j in range(len(Arr) - i - 1):
            if Arr[j] >= Arr[j + 1]:
                Arr[j], Arr[j + 1] = Arr[j + 1], Arr[j]
    return tuple(Arr)