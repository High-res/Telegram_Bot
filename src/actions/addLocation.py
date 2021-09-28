import pymysql
import config

def addLocation(user_name, user_tg_id, location_latitude, location_longitude, send_date, day, year_month) :
    try: 
        connection = pymysql.connect(
                host=config.host, 
                port=3306,
                user=config.user,
                password=config.password,
                database=config.db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
        print('Location connected!')
        # Наже создаем бд users и в таблицу записываем id name и password 
        try :
            with connection.cursor() as cursor :
                insert_query = "INSERT INTO `user_location` (user_name, user_tg_id, location_latitude, location_longitude, send_date, date, date_today) VALUES (%s,%s,%s,%s,%s,%s,%s);" 
                cursor.execute(insert_query, (user_name, user_tg_id, location_latitude, location_longitude, send_date, day, year_month))
                connection.commit()
            print('Location connected inside!')
        finally:
            connection.close()
    except Exception as ex :
        print("Failed to connection ...")
        print(ex)
