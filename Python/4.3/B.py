def recursive_digit_sum(n):
    if not n:
        return 0
    return (n % 10) + recursive_digit_sum(n // 10)