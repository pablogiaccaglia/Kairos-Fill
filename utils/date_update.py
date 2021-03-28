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
    row = ((dayToBook - 1) // 7) + 1
    column = dayToBook - 7 * (row - 1)

    if num == 4 or num == 5:
        flag = 0

    telegram_users_database.UsersDatabase.add_date(day, month, flag, row, column)
    print("done")


dateUpdater()
