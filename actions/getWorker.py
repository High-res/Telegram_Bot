
import pymysql
import config


def getWorkerss() :
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
                select_all_rows = "SELECT * FROM `workers`"
                cursor.execute(select_all_rows)
                workers = cursor.fetchall()
                # for row in workers :
                #     print(row)
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось getWorkers.py")
        print(ex)

    return workers


# async def schedulers() :
#     print('Worked')
# async def on_startup(_) :
#     asyncio.create_task(schedulers())