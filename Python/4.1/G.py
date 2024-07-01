def can_eat(Horse, enemy):
    if Horse[0] + 1 == enemy[0] and Horse[1] + 2 == enemy[1]:
        return True
    if Horse[0] + 1 == enemy[0] and Horse[1] - 2 == enemy[1]:
        return True
    if Horse[0] + 2 == enemy[0] and Horse[1] + 1 == enemy[1]:
        return True
    if Horse[0] + 2 == enemy[0] and Horse[1] - 1 == enemy[1]:
        return True
    if Horse[0] - 1 == enemy[0] and Horse[1] + 2 == enemy[1]:
        return True
    if Horse[0] - 1 == enemy[0] and Horse[1] - 2 == enemy[1]:
        return True
    if Horse[0] - 2 == enemy[0] and Horse[1] + 1 == enemy[1]:
        return True
    if Horse[0] - 2 == enemy[0] and Horse[1] - 1 == enemy[1]:
        return True
    return False