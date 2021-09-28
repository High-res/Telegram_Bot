import pymysql
import config


def getAvans(user_name, user_tg_id, answer, time) :
    try: 
        connection = pymysql.connect(
                host=config.host, 
                port=3306,
                user=config.user,
                password=config.password,
                database=config.db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
        # Наже создаем бд users и в таблицу записываем id name и password 
        try :
            with connection.cursor() as cursor :
                insert_query = "INSERT INTO `avans_from_user` (user_name, user_tg_id, answer, date) VALUES (%s,%s,%s,%s);" 
                cursor.execute(insert_query, (user_name, user_tg_id, answer, time))
                connection.commit()
                print('Заявление на аванс отправлен!')
        finally:
            connection.close()
    except Exception as ex :
        print("Failed to connection ...")
        print(ex)

def getAvanses() :
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
                select_all_rows = "SELECT * FROM `avans_from_user`"
                cursor.execute(select_all_rows)
                rowAvans = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowAvans


