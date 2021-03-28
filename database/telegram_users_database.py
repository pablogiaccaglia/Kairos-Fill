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
            user_dict = {}
            user_dict['Nome'] = (user[0])
            user_dict['Mail'] = user[1]
            user_dict['CodMatricola'] = str(user[2])
            user_dict['Telefono'] = int(user[3])
            user_dict['Biblioteca'] = user[4]
            user_dict['Aula'] = user[5]
            user_dict['user_id'] = str(user[6])
            users.append(user_dict)

        mycursor.close()
        MYDB.close()

        return users

    def add_user(self, name, mail, student_id, phone, library, hall, user_id):
        MYDB = mysql.connector.connect(
            host=UsersDatabase.HOST,
            user=UsersDatabase.USER,
            password=UsersDatabase.PASSWORD,
            database=UsersDatabase.DATABASE
        )
        sql = "INSERT INTO users (Nome, Mail, CodMatricola, Telefono, Biblioteca, Aula, chat_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (self, name, mail, student_id, phone, library, hall, user_id)
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
            user_info = {}
            user_info['Nome'] = user[0]
            user_info['Mail'] = user[1]
            user_info['CodMatricola'] = str(user[2])
            user_info['Telefono'] = int(user[3])
            user_info['Biblioteca'] = user[4]
            user_info['Aula'] = user[5]
            user_info['user_id'] = str(user[6])
            user_info_dict.append(user_info)

        return user_info_dict
