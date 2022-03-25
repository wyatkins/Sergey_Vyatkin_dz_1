def transform_string(number: int) -> str:
    if number == 1 or number == 21 or number == 31 or number == 41 \
            or number == 51 or number == 61 or number == 71 or number == 81 or number == 91:
        return f"{number} процент"
    elif number == 2 or number == 22 or number == 32 or number == 42 \
            or number == 52 or number == 62 or number == 72 or number == 82 or number == 92:
        return f"{number} процента"
    elif number == 3 or number == 23 or number == 33 or number == 43 or number == 53 \
            or number == 63 or number == 73 or number == 83 or number == 93:
        return f"{number} процента"
    elif number == 4 or number == 24 or number == 34 or number == 44 or number == 54 \
            or number == 64 or number == 74 or number == 84 or number == 94:
        return f"{number} процента"
    else:
        return f"{number} процентов"


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))