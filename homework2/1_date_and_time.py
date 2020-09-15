"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta


def print_days():

    today = datetime.now()
    delta = 30
    str_format = '%d.%m.%Y'

    print('Today is {}'.format(today.strftime(str_format)))
    print('Yesterday was {}'.format(
        (today - timedelta(1)).strftime(str_format))
        )
    print('{} days ago was {}'.format(
        delta, (today - timedelta(delta)).strftime(str_format))
        )


def str_2_datetime(date_string):

    return datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
