import pymysql

import config


def get_text() :
    try :
        connection = pymysql.connect(
            host=config.HOST, 
            port=3306,
            user=config.USER,
            password=config.PASSWORD,
            database=config.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `message_for_bot`"
                cursor.execute(select_all_rows)
                rowText = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowText