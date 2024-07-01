def make_matrix(lenght, value=0):
    if isinstance(lenght, int):
        return [[value] * lenght for i in range(lenght)]
    else:
        return [[value] * lenght[0] for i in range(lenght[1])]