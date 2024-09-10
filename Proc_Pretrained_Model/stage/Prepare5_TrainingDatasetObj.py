import mysql
import pandas as pd
import Variable as var
import pickle
import commons.mysql.mysqlHelper as sqlHelper

col_name = ['id', 'lang_type', 'ori_text', 'mul_text', 'lang_col', 'label', 'plabel']

def select_data_from_synthetic_dataset(langType, size):
    id_List = []
    lang_type_List = []
    ori_text_List = []
    mul_text_List = []
    lang_col_List = []
    label_List = []
    plabel_List = []

    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        sql = ("select id, lang_type, ori_text, mul_text, lang_col, label, plabel from synthetic_text where lang_type = '" + langType + str(size) + "'")
        mycursor.execute(sql)
        result = mycursor.fetchall()

        cnt = 0
        for i in result:
            id_List.append(i[0])
            lang_type_List.append(i[1])
            ori_text_List.append(i[2])
            mul_text_List.append(i[3])
            lang_col_List.append(i[4])
            label_List.append(i[5])
            plabel_List.append(i[6])
            cnt = cnt + 1

        print("Settle count: " + str(cnt))


    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    dict = {'id': id_List, 'lang_type': lang_type_List, 'ori_text': ori_text_List, 'mul_text': mul_text_List, 'lang_col': lang_col_List, 'label': label_List, 'plabel': plabel_List}


    df = pd.DataFrame(dict)

    print(df.head(10))


Selected_Size_list = [var.SAMPLING_400, var.SAMPLING_1600, var.SAMPLING_2800]
lang_type_list = ['E', 'M']


df = select_data_from_synthetic_dataset("E", 400)