"""
Load the testing dataset object from binary file and save it into eva_eng_text and eva_mul_text.
"""

import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector
import Variable as var
import pickle
def insert_val_eng_ds(dataDF):

    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        insert_sql = """
                insert into eva_eng_text (
                clean_text, label
                ) values (
                %s, %s )

                """
        values = []

        print(type(dataDF))
        for index, row in dataDF.iterrows():
            tuppleData = (row['cleanedtxt'], var.Label_Code_Desc[int(row['std_label'])])
            values.append(tuppleData)

        # executemany() method
        mycursor.executemany(insert_sql, values)
        # save changes
        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

def insert_val_mul_ds(dataDF):

    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        insert_sql = """
                insert into eva_mul_text (
                clean_text, label
                ) values (
                %s, %s )

                """
        values = []

        print(type(dataDF))
        for index, row in dataDF.iterrows():
            tuppleData = (row['multilang_text'], var.Label_Code_Desc[int(row['std_label'])])
            values.append(tuppleData)

        # executemany() method
        mycursor.executemany(insert_sql, values)
        # save changes
        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

def prepare_table(OUTPUT_PATH, LANG_TYPE):
    file_name = "Val_DS_" + LANG_TYPE + "_" + str(DATA_SIZE) + ".obj"
    print(file_name)
    fileObj = open(OUTPUT_PATH + file_name, 'rb')
    print(fileObj)
    df = pickle.load(fileObj)
    fileObj.close()
    return df

LANG_TYPE_LIST = [var.LANG_TYPE_ENG, var.LANG_TYPE_MULTI]
DATA_SIZE = var.SAMPLING_2800
OUTPUT_PATH = "../output/"

for LANG_TYPE in LANG_TYPE_LIST:
    df = prepare_table(OUTPUT_PATH, LANG_TYPE)
    if LANG_TYPE == var.LANG_TYPE_ENG:
        print(df.head(5))
        insert_val_eng_ds(df)
    if LANG_TYPE == var.LANG_TYPE_MULTI:
        print(df.head(5))
        insert_val_mul_ds(df)
