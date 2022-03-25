def convert_time(duration: int) -> str:
    # из duration получаем количество дней (целых)
    transform_to_days = duration // (24 * 3600)

    # получаем остаток от transform_duration_to_days (в секундах)
    rest_days = duration % (24 * 3600)

    # остаток переводим в часы (целых)
    hours = rest_days // 3600

    # получаем остаток от часов (в секундах)
    rest_hourse = rest_days % 3600

    # остаток переводим в минуты (в секундах)
    minute = rest_hourse // 60

    # получаем остаток от минут (в секундах)
    rest_sec = rest_hourse % 60

    if duration >= 24 * 3600:
        #return transform_to_days, hours, minute, rest_sec
        return f"{transform_to_days} дн {hours} час {minute} мин {rest_sec} сек"
    elif duration >= 3600:
        #return hours, minute, rest_sec
        return f"{hours} час {minute} мин {rest_sec} сек"
    elif duration >= 60:
        #return minute, rest_sec
        return f"{minute} мин {rest_sec} сек"
    else:
        #return rest_sec
        return f"{rest_sec} сек"


duration = 400153
result = convert_time(duration)

print(result)