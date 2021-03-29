import os
import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            user_id INT,
            user_pw VARCHAR(255),
            chat_id INT NOT NULL,
            PRIMARY KEY(user_id, user_pw)
        )
         """
    )

    conn = None

    try:
        DATABASE_URL = os.environ[
            'postgres://bawkwgdetghigk:171742fdd917757f31c2eed21580bd8008e142e0a07ef64d26bc3b01166a9761@ec2-54-228-9-90.eu-west-1.compute.amazonaws.com:5432/d2ka7f1q4au9tm']

        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
