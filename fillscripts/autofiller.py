# -*- coding: utf-8 -*-
from nightFiller import KairosBot
from database.telegram_users_database import UsersDatabase


# sched = BlockingScheduler()

def autofiller():
    users = UsersDatabase.get_users()
    print(users)
    kairos = KairosBot()

    for user in users:
        print(user['student_id'] + " " + user['user_pw'])
        kairos.fillerUserData(user['student_id'], user['user_pw'], user['library'], user['hall'])
        kairos.resetBot()


if __name__ == '__main__':
    autofiller()
