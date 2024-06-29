while Str := input():
    if not Str.startswith('#'):
        print(Str[:x if (x := Str.find('#')) != -1 else len(Str)])