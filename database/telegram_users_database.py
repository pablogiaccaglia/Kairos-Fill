# -*- coding: utf-8 -*-
"""
Created on
@author: pablo
"""

### MODULES

import mysql.connector


# Database

class UsersDatabase:
    HOST = "michaelfareshi.mysql.pythonanywhere-services.com"
    USER = "michaelfareshi"
    PASSWORD = "pepsikola"
    DATABASE = "michaelfareshi$datiUtente"

    def get_users(self):
        MYDB = mysql.connector.connect(
            host=UsersDatabase.HOST,
            user=UsersDatabase.USER,
            password=UsersDatabase.PASSWORD,
            database=UsersDatabase.DATABASE
        )
        mycursor = MYDB.cursor()
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()
        users = []

        for user in myresult:
            user_dict = {
                'CodMatricola': str(user[2]),
                'Password': int(user[3]),
                'Biblioteca': user[4],
                'Aula': user[5],
                'user_id': str(user[6])
                         }
            users.append(user_dict)

        mycursor.close()
        MYDB.close()

        return users

    def add_user(self, student_id, password, library, hall, user_id):
        MYDB = mysql.connector.connect(
            host=UsersDatabase.HOST,
            user=UsersDatabase.USER,
            password=UsersDatabase.PASSWORD,
            database=UsersDatabase.DATABASE
        )
        sql = "INSERT INTO users (CodMatricola, Password, Biblioteca, Aula, chat_id) VALUES (%s,%s,%s,%s,%s)"
        val = (self, student_id, password, library, hall, user_id)
        mycursor = MYDB.cursor()
        mycursor.execute(sql, val)
        MYDB.commit()
        mycursor.close()
        MYDB.close()

    def delete_user(self, student_id):
        MYDB = mysql.connector.connect(
            host=UsersDatabase.HOST,
            user=UsersDatabase.USER,
            password=UsersDatabase.PASSWORD,
            database=UsersDatabase.DATABASE
        )

        sql = f"DELETE FROM users WHERE CodMatricola={student_id}"
        mycursor = MYDB.cursor()
        mycursor.execute(sql)
        MYDB.commit()
        mycursor.close()
        MYDB.close()

    def add_date(self, day, month, flag, row, column):
        MYDB = mysql.connector.connect(
            host=UsersDatabase.HOST,
            user=UsersDatabase.USER,
            password=UsersDatabase.PASSWORD,
            database=UsersDatabase.DATABASE
        )

        sql = f"UPDATE date SET DAY={day}, MONTH={month}, FLAG={flag}, ROW={row}, COL={column}"
        mycursor = MYDB.cursor()
        mycursor.execute(sql)
        MYDB.commit()
        mycursor.close()
        MYDB.close()

    def get_date(self):
        MYDB = mysql.connector.connect(
            host=UsersDatabase.HOST,
            user=UsersDatabase.USER,
            password=UsersDatabase.PASSWORD,
            database=UsersDatabase.DATABASE
        )

        mycursor = MYDB.cursor()
        mycursor.execute("SELECT * FROM date")
        date = mycursor.fetchall()

        return date[0]

    def get_user(self, chat_id):
        MYDB = mysql.connector.connect(
            host=UsersDatabase.HOST,
            user=UsersDatabase.USER,
            password=UsersDatabase.PASSWORD,
            database=UsersDatabase.DATABASE
        )

        mycursor = MYDB.cursor()
        mycursor.execute(f"SELECT * FROM users WHERE chat_id = {chat_id}")
        myresult = mycursor.fetchall()
        mycursor.close()
        MYDB.close()

        user_info_dict = []

        for user in myresult:
            user_info = {
                'CodMatricola': str(user[0]),
                'Password': int(user[1]),
                'Biblioteca': user[2],
                'Aula': user[3],
                'user_id': str(user[4])
            }
            user_info_dict.append(user_info)

        return user_info_dict
