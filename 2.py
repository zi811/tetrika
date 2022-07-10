def task(x1, y1, x2, y2, x3, y3, x4, y4):
    left = max(x1, x3)
    top = min(y2, y4)
    right = min(x2, x4)
    bottom = max(y1, y3)

    width = right - left
    height = top - bottom

    if width < 0 or height < 0:
        return False

    return True


print(task(1, 1, 2, 2, 3, 3, 4, 4))

"""поиск площадь пересечения"""


def task1(x1, y1, x2, y2, x3, y3, x4, y4):
    left = max(x1, x3)
    top = min(y2, y4)
    right = min(x2, x4)
    bottom = max(y1, y3)

    width = right - left
    height = top - bottom

    if width < 0 or height < 0:
        return 0

    return width * height


print(task1(1, 1, 2, 2, 3, 3, 4, 4))
