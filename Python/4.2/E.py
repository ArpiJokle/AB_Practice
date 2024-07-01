def to_string(*args, **kwargs):
    Sep = kwargs.get("sep", " ")
    End = kwargs.get("end", "\n")
    return Sep.join([str(i) for i in args]) + End