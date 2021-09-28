import pymysql
import config


def getChallenge() :
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
                select_all_rows = "SELECT * FROM `bot_challenges`"
                cursor.execute(select_all_rows)
                rowChallenge = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowChallenge

def addChallengeAction(challenge, answer, tg_id, date, date2) :
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
            # insert добавить пользователей 
            with connection.cursor() as cursor :
                insert_query = "INSERT INTO `bot_challenges_actions` (challenge, answer, tg_id, date, date2) VALUES (%s,%s,%s,%s,%s);"
                cursor.execute(insert_query, (challenge, answer, tg_id, date, date2))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)


def getChallengeAction() :
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
                select_all_rows = "SELECT * FROM `bot_challenges_actions`"
                cursor.execute(select_all_rows)
                rowChallenge = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowChallenge