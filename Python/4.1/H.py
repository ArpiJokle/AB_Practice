def is_palindrome(Input):
    if isinstance(Input, int):
        return str(Input) == str(Input)[::-1]
    return Input == Input[::-1]