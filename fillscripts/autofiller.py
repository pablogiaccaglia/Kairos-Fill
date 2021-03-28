# -*- coding: utf-8 -*-
from nightFiller import fillerUserData
from database.telegram_users_database import UsersDatabase
from utils import date_update


if __name__ == '__main__':

    date_update.dateUpdater()
    date = UsersDatabase.get_date()
    users = UsersDatabase.get_users()
    flag = date[2]
    row = date[3]
    column = date[4]

    for user in users:
        print("ciao")
        fillerUserData(user['Aula'],user['Nome'], user['Mail'], user['CodMatricola'], user['Telefono'], row, column)


