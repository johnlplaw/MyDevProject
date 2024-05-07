import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector

def is_model_done(model_name):
    print("Start to query ...")
    isFound = False;
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = """
                    select count(1) from model_training where model_name = %s
                    """
        val = (model_name,)
        mycursor.execute(Select_sql, val)
        result = mycursor.fetchone()
        isFound = result[0] > 0

        print("Finish query ...")
    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return isFound


Result = is_model_done("Chk-FB-XLM-R_English_1200_0.001")
print(Result)