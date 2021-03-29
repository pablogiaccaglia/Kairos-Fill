# -*- coding: utf-8 -*-
from nightFiller import fillerUserData
from database.telegram_users_database import UsersDatabase
from utils import date_update
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def autofiller():
    # date_update.dateUpdater()
    # date = UsersDatabase.get_date()
    users = UsersDatabase.get_users()
    #    flag = date[2]
    # row = date[3]
    # column = date[4]
    row = 6
    column = 3
    for user in users:
        print("ciao")
        fillerUserData(user['student_id'], user['user_pw'], user['library'], user['hall'], row, column)




if __name__ == '__main__':
    sched.start()
