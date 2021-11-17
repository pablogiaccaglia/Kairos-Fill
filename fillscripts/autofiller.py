# -*- coding: utf-8 -*-
import time

import schedule as schedule

from nightFiller import KairosBot
from database.users_database import UsersDatabase


# sched = BlockingScheduler()

def autofiller():
    users = UsersDatabase.get_users()
    print(users)
    kairos = KairosBot()
    kairos.start(kairos.SINGLE_BOOK)


# schedule.every().day.at("00:01").do(autofiller)

if __name__ == '__main__':
    # while True:
    #     schedule.run_pending()
    #  print("hello")
    #     time.sleep(1)
    autofiller()
