def number_length(n):
    count = 0
    m = abs(n)
    while m:
        count += 1
        m //= 10
    return count