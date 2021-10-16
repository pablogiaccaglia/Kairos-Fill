# -*- coding: utf-8 -*-
"""
Created on
@author: pablo
"""

### MODULES
import os
import psycopg2


# Database

class UsersDatabase:
    HOST = "ec2-54-228-9-90.eu-west-1.compute.amazonaws.com"
    USER = "bawkwgdetghigk"
    PASSWORD = "171742fdd917757f31c2eed21580bd8008e142e0a07ef64d26bc3b01166a9761"
    DATABASE = "d2ka7f1q4au9tm"

    @staticmethod
    def __dbconnect():
        MYDB = psycopg2.connect(
            host=UsersDatabase.HOST,
            user=UsersDatabase.USER,
            password=UsersDatabase.PASSWORD,
            database=UsersDatabase.DATABASE
        )
        return MYDB




    @staticmethod
    def get_users():
        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()
        users = []

        for user in myresult:
            user_dict = {
                'student_id': str(user[0]),
                'user_pw': (user[1]),
                'library': user[2],
                'hall': user[3],
                'user_id': str(user[4])
            }
            users.append(user_dict)

        mycursor.close()
        MYDB.close()

        return users

    @staticmethod
    def add_user(student_id, password, library, hall, user_id):

        sql = "INSERT INTO users (user_id, user_pw, library, hall, chat_id) VALUES (%s,%s,%s,%s,%s)"
        val = (student_id, password, library, hall, user_id)
        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute(sql, val)
        MYDB.commit()
        mycursor.close()
        MYDB.close()

    @staticmethod
    def delete_user(student_id):

        sql = f"DELETE FROM users WHERE user_id={student_id}"
        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute(sql)
        MYDB.commit()
        mycursor.close()
        MYDB.close()



    @staticmethod
    def get_date():

        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute("SELECT * FROM date")
        date = mycursor.fetchall()
        mycursor.close()
        MYDB.close()
        return date[0]

    @staticmethod
    def get_user(chat_id):

        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute(f"SELECT * FROM users WHERE chat_id = {chat_id}")
        myresult = mycursor.fetchall()
        mycursor.close()
        MYDB.close()

        user_info_dict = []

        for user in myresult:
            user_info = {
                'CodMatricola': str(user[0]),
                'Password': (user[1]),
                'Biblioteca': user[2],
                'Aula': user[3],
                'user_id': str(user[4])
            }
            user_info_dict.append(user_info)

        return user_info_dict
