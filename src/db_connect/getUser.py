import pymysql

import config


def get_user() :
    try: 
        connection = pymysql.connect(
            host=config.HOST, 
            port=3306,
            user=config.USER,
            password=config.PASSWORD,
            database=config.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        # Наже создаем бд users и в таблицу записываем id name и password 
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `telegram_users`"
                cursor.execute(select_all_rows)
                telegram_users = cursor.fetchall()
            # insert добавить пользователей 
        finally:
            connection.close()
    except Exception as ex :
        print("Failed to connection ...")
        print(ex)
    return telegram_users

def add_user(user_name, user_id, register_date) :
    try: 
        connection = pymysql.connect(
            host=config.HOST, 
            port=3306,
            user=config.USER,
            password=config.PASSWORD,
            database=config.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        # Наже создаем бд users и в таблицу записываем id name и password 
        try :
           with connection.cursor() as cursor :
                insert_query = "INSERT INTO `telegram_users` (name, tg_id, register_date) VALUES (%s,%s,%s);" 
                cursor.execute(insert_query, (user_name, user_id, register_date))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Failed to connection ...")
        print(ex)