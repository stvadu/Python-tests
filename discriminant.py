def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return (b ** 2 - (4 * a * c))


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) < 0:
        return 'корней нет'
    elif discriminant(a, b, c) == 0:
        x = (-b) / (2 * a)
        return x
    else:
        x_1 = (- b + discriminant(a, b, c) ** 0.5) / (2 * a)
        x_2 = (- b - discriminant(a, b, c) ** 0.5) / (2 * a)
        return (x_1, x_2)


if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))