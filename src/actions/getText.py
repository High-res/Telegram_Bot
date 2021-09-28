import pymysql
import config


def getText() :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
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