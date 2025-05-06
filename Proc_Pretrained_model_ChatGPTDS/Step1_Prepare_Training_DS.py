import mysql.connector

import commons.mysql.mysqlHelper as sqlHelper
from commons.DataClass.DataClass import GPTTextData
import commons.DataClass.Variable as var

import pickle

"""
This script is for generating the training dataset for each emotion with count 400, 1600 and 2800
"""


def Get_ChatGPT_Data():
    """
    Get the unlabelled ChatGPT generated data from database
    :return:
    """

    TextList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        sql = ("select id, ori_text, label, pseudo_label from ChatGPT_text order by id")
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            txt = i[1]
            label = var.Label_Desc_Code[i[2]]
            plabel = var.Label_Desc_Code[i[3]]
            data = GPTTextData(id, txt, label, plabel)
            TextList.append(data)

    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return TextList

# Step 1: Load the data
the_data = Get_ChatGPT_Data()
print("Total record found: ")
print(len(the_data))

# Step 2: Generate the list object as a binary file
fileObj = open(var.FILE_NOSAMPLING_CHATGPT_TEXT_DATASET, 'wb')
pickle.dump(the_data, fileObj)
fileObj.close()