import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector
from translate_shell.translate import translate
import commons.emotion.identifyEmotion as emo
from commons.DataClass.DataClass import GPTTextData

"""
This script is for providing the pseudo labeling by text2emotion.
"""

def Get_Unlabeled_Text():
    """
    Get the unlabelled ChatGPT generated data from database
    :return:
    """
    TextList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        sql = ("select id, ori_text from emotion_text where In_English is null LIMIT 50")
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            tweet = i[1]
            data = GPTTextData(id, tweet)
            TextList.append(data)

    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return TextList


def translate_text(dataList):
    for dt in dataList:
        translate_en = translate(dt.text, source_lang="auto", target_lang="en").results[0].paraphrase
        emotion_detected = emo.identifyEmotion(translate_en)
        print(translate_en + " - " + emotion_detected)
        dt.inEnglish = translate_en
        dt.pseudoLabel = emotion_detected

    return dataList


def Update_GPTText_pseudolabel(processedList):
    """
    Update the pseudo label
    :param processedList: Processed tweets pseudo label
    """
    conn = sqlHelper.get_mysql_conn()
    mycursor = conn.cursor()
    try:
        sql = ("update emotion_text set In_English = %s, pseudo_label = %s where id = %s")

        for txt in processedList:
            val = (txt.inEnglish, txt.pseudoLabel, txt.id)
            mycursor.execute(sql, val)

        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

while True:
    # Step 1: Get the data from table
    Data_List = Get_Unlabeled_Text()

    if len(Data_List) == 0 :
        break

    # Step 2: Translate into English, and pseudo label
    Data_List = translate_text(Data_List)
    # Step 3: Update the English text and pseudo label back to database
    Update_GPTText_pseudolabel(Data_List)