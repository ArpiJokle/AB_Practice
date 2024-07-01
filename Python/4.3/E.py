def result_accumulator(f):
    List = []
    
    def decotator(*args, method="accumulate"):
        nonlocal List
        List.append(f(*args))
        if "accumulate" != method:
            temp = List
            List = []
            return temp
    return decotator