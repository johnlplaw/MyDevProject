import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector

def get_model_list(model_name):
    print("Start to query ...")
    acc_training_list = []
    acc_evaluation_list = []

    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = """
                select round(training_accuracy, 4) as training_accuracy, round(val_accuracy, 4) as val_accuracy 
                from model_training 
                where model_name = %s 
                order by epoch;
                """
        val = (model_name,)
        mycursor.execute(Select_sql, val)
        result = mycursor.fetchall()

        for i in result:
            acc_training = i[0]
            acc_evaluation = i[1]

            acc_training_list.append(acc_training)
            acc_evaluation_list.append(acc_evaluation)

        print("Finish query ...")
    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return acc_training_list, acc_evaluation_list
