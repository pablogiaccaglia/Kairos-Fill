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
                host = UsersDatabase.HOST,
                user = UsersDatabase.USER,
                password = UsersDatabase.PASSWORD,
                database = UsersDatabase.DATABASE
        )

        return MYDB

    @staticmethod
    def get_users():
        query = "SELECT * FROM users"
        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        users = []

        for user in myresult:
            user_dict = {
                'student_id': str(user[0]),
                'user_pw':    (user[1]),
                'library':    user[2],
                'hall':       user[3],
                'user_id':    str(user[4]),
                'secondary_hall': str(user[5])
            }
            users.append(user_dict)

        mycursor.close()
        MYDB.close()

        return users

    @staticmethod
    def add_user(student_id, password, library, hall, user_id):

        query = "INSERT INTO users (user_id, user_pw, library, hall, chat_id) VALUES (%s,%s,%s,%s,%s)"
        val = (student_id, password, library, hall, user_id)
        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute(query, val)
        MYDB.commit()
        mycursor.close()
        MYDB.close()

    @staticmethod
    def delete_user(student_id):

        query = f"DELETE FROM users WHERE user_id={student_id}"
        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute(query)
        MYDB.commit()
        mycursor.close()
        MYDB.close()

    @staticmethod
    def get_date():

        query = "SELECT * FROM date"
        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute(query)
        date = mycursor.fetchall()
        mycursor.close()
        MYDB.close()
        return date[0]

    @staticmethod
    def get_user(user_id):

        query = f"SELECT * FROM users WHERE user_id = {user_id}"
        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        MYDB.close()

        user_info_dict = []

        for user in myresult:
            user_info = {
                'CodMatricola': str(user[0]),
                'Password':     (user[1]),
                'Biblioteca':   user[2],
                'Aula':         user[3],
                'user_id':      str(user[4])
            }
            user_info_dict.append(user_info)

        return user_info_dict

    def add_secondary_hall_option_to_all(self):
      #  UsersDatabase.add_column_to_users_table("secondary_hall", "VARCHAR(64)")
        users = db.get_users()
        MYDB = UsersDatabase.__dbconnect()

        for user in users:

            if user['library'] == "Biblioteca di Lettere":
                new_hall = "Biblioteca di Lettere - Sala filosofia 2"
                UsersDatabase.add_secondary_hall_option(user['student_id'], new_hall, MYDB)

            elif user['library'] == "Biblioteca di Scienze Sociali":
                new_hall = "Biblioteca di Scienze sociali - Sale Secondo piano"
                UsersDatabase.add_secondary_hall_option(user['student_id'], new_hall, MYDB)

        MYDB.close()
        pass

    @staticmethod
    def add_secondary_hall_option(student_id, hall, MYDB = None):

        closeConnection = False
        query = """UPDATE users
                            SET secondary_hall = '{0}'
                            WHERE user_id = {1};""".format(hall, student_id)

        if MYDB is None:
            MYDB = UsersDatabase.__dbconnect()
            closeConnection = True

        mycursor = MYDB.cursor()
        mycursor.execute(query)
        MYDB.commit()
        mycursor.close()

        if closeConnection:
            MYDB.close()

    @staticmethod
    def add_column_to_users_table(name, type):

        query = """ALTER TABLE users
                            ADD {0} {1};""".format(name, type)

        MYDB = UsersDatabase.__dbconnect()
        mycursor = MYDB.cursor()
        mycursor.execute(query)
        MYDB.commit()
        mycursor.close()
        MYDB.close()


if __name__ == '__main__':
    db = UsersDatabase()
    users = db.get_users()
    usersSorted = sorted(users, key = lambda k: k['hall'])
    for user in usersSorted:
        print(user['student_id'] + ": " + user["user_pw"] + ' | ' + user['library'] + " -> " + user['hall'] + " | " + user['secondary_hall'])
#  db.delete_user(7050361)
# db.add_user(7076088, "Balotelli01!",  "Biblioteca di Lettere", "Biblioteca di Lettere - Sala italianistica e spettacolo",  111111111)

