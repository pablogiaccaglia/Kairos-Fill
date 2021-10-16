# -*- coding: utf-8 -*-
# !/home/michaelfareshi/.virtualenvs/myvenv/bin/python3.8
from datetime import datetime
from database import telegram_users_database


def dateUpdater():
    today = datetime.today()
    day = today.day
    dayToBook = day + 2
    month = today.month
    num = today.weekday()
    flag = 1
    row = ((dayToBook - 1) // 7) + 2
    column = dayToBook - 7 * (row - 2)

    print(row)
    print(column)

    if num == 4 or num == 5:
        flag = 0


if __name__ == '__main__':
    dateUpdater()
# dateUpdater()
