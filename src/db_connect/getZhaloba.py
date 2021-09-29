import pymysql

import config


def get_zhaloba(user_name, user_tg_id, answer, time) :
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
                insert_query = "INSERT INTO `zhaloba_from_user` (user_name, user_tg_id, answer, date) VALUES (%s,%s,%s,%s);" 
                cursor.execute(insert_query, (user_name, user_tg_id, answer, time))
                connection.commit()
                print('Жалоба отправлена')
        finally:
            connection.close()
    except Exception as ex :
        print("Failed to connection ...")
        print(ex)
