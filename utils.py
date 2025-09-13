from calendar import month
import datetime


def get_date_from_string(string):
    """Извлекает дату из строки типа '14 часов назад' и time: '10:00'."""
    now = datetime.datetime.now().replace(second=0, microsecond=0)

    if string == "вчера":
        return now - datetime.timedelta(days=1)

    words = string.split()

    amount = 1
    if len(words) == 3:
        amount = int(words[0]) if words[0].isdigit() else 1

    unit = words[1]

    if unit in ['час', 'часа', 'часов']:
        return now - datetime.timedelta(hours=amount)
    elif unit in ['минуту', 'минуты', 'минут', 'минута']:
        return now - datetime.timedelta(minutes=amount)
    elif unit in ['секунду', 'секунды', 'секунд', 'секунда', 'сек.']:
        return now - datetime.timedelta(seconds=amount)
    elif unit in ['день', 'дней', 'дня', 'дн.']:
        return now - datetime.timedelta(days=amount)
    elif unit in ['неделю', 'недели', 'недель', 'неделя', 'нед.']:
        return now - datetime.timedelta(weeks=amount)
    else:
        return now - datetime.timedelta(days=365)
