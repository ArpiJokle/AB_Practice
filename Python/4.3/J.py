def make_linear(List):
    Answer = []
    for i in List:
        if isinstance(i, int):
            Answer.append(i)
        else:
            Answer.extend(make_linear(i))
    return Answer
