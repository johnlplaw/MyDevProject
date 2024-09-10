"""
This script is for labelling the testing dataset, stored in eva_eng_text and eva_mul_text tables, with pseudo-labeling
by text2emotion library.
"""

import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector
import PTM_lib as ptm
import pickle
import Variable as var
import commons.emotion.identifyEmotion as emo

MODEL_MBERT_ENG = "mbert_eng"
MODEL_MBERT_MUL = "mbert_mul"
MODEL_XLMR_ENG = "xlmr_eng"
MODEL_XLMR_MUL = "xlmr_mul"

# Column name for redicted result
COL_MBERT_ENG_400 = "mbert_eng_400"
COL_MBERT_ENG_1600 = "mbert_eng_1600"
COL_MBERT_ENG_2800 = "mbert_eng_2800"
COL_MBERT_MUL_400 = "mbert_mul_400"
COL_MBERT_MUL_1600 = "mbert_mul_1600"
COL_MBERT_MUL_2800 = "mbert_mul_2800"
COL_XLMR_ENG_400 = "xlmr_eng_400"
COL_XLMR_ENG_1600 = "xlmr_eng_1600"
COL_XLMR_ENG_2800 = "xlmr_eng_2800"
COL_XLMR_MUL_400 = "xlmr_mul_400"
COL_XLMR_MUL_1600 = "xlmr_mul_1600"
COL_XLMR_MUL_2800 = "xlmr_mul_2800"


LANG_TYPE_LIST = [var.LANG_TYPE_ENG, var.LANG_TYPE_MULTI]
DATA_SIZE = var.SAMPLING_2800
OUTPUT_PATH = "../output/"

class Selected_Model:
    """
    Model info.
    """
    def __init__(self, fileName, modelName, colName):
        self.fileName = fileName
        self.modelName = modelName
        self.colName = colName

e_mBert_400 = Selected_Model("Final-mBERT_English_400_1e-05_model.pth", "mBERT-400", COL_MBERT_ENG_400)
e_mBert_1600 = Selected_Model("Final-mBERT_English_1600_1e-05_model.pth", "mBERT-1600", COL_MBERT_ENG_1600)
e_mBert_2800 = Selected_Model("Final-mBERT_English_2800_1e-05_model.pth", "mBERT-2800", COL_MBERT_ENG_2800)
e_fbXLMr_400 = Selected_Model("Final-FB-XLM-R_English_400_1e-05_model.pth", "FB-XLM-R-400", COL_XLMR_ENG_400)
e_fbXLMr_1600 = Selected_Model("Final-FB-XLM-R_English_1600_1e-05_model.pth", "FB-XLM-R-1600", COL_XLMR_ENG_1600)
e_fbXLMr_2800 = Selected_Model("Final-FB-XLM-R_English_2800_1e-05_model.pth", "FB-XLM-R-2800", COL_XLMR_ENG_2800)
m_mBert_400 = Selected_Model("Final-mBERT_Multilingual_400_1e-05_model.pth", "mBERT-400", COL_MBERT_MUL_400)
m_mBert_1600 = Selected_Model("Final-mBERT_Multilingual_1600_1e-05_model.pth", "mBERT-1600", COL_MBERT_MUL_1600)
m_mBert_2800 = Selected_Model("Final-mBERT_Multilingual_2800_1e-05_model.pth", "mBERT-2800", COL_MBERT_MUL_2800)
m_fbXLMr_400 = Selected_Model("Final-FB-XLM-R_Multilingual_400_1e-05_model.pth", "FB-XLM-R-400", COL_XLMR_MUL_400)
m_fbXLMr_1600 = Selected_Model("FInal-FB-XLM-R_Multilingual_1600_1e-05_model.pth", "FB-XLM-R-1600", COL_XLMR_MUL_1600)
m_fbXLMr_2800 = Selected_Model("Final-FB-XLM-R_Multilingual_2800_1e-05_model.pth", "FB-XLM-R-2800", COL_XLMR_MUL_2800)

mbert_model_list = [e_mBert_400, e_mBert_1600, e_mBert_2800, m_mBert_400, m_mBert_1600, m_mBert_2800]
xmlr_model_list = [e_fbXLMr_400, e_fbXLMr_1600, e_fbXLMr_2800, m_fbXLMr_400, m_fbXLMr_1600, m_fbXLMr_2800]

class EvaTextData:
    id = ""
    clean_text = ""
    pseudo_label = ""

    def __int__(self, id, clean_text):
        self.id = id
        self.clean_text = clean_text

    def setPredictedLabel(self, pseudo_label):
        self.pseudo_label = pseudo_label


def select_eval_data(tableStr):
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        select_sql = "SELECT ID, CLEAN_TEXT FROM " + tableStr + " order by ID"
        mycursor.execute(select_sql)
        myresult = mycursor.fetchall()
        dataList = []

        for x in myresult:
            data = EvaTextData()
            data.id = str(x[0])
            data.clean_text = x[1]
            dataList.append(data)

    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")
    return dataList

def update_pseudo_label(tableStr, datalist):
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        update_sql = "UPDATE " + tableStr + " set pseudo_label = %s where id = %s "
        values = []

        for evaTextData in datalist:
            tuppleData = (evaTextData.pseudo_label, evaTextData.id)
            values.append(tuppleData)

        # executemany() method
        mycursor.executemany(update_sql, values)
        # save changes
        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")


EngdataList = select_eval_data("eva_eng_text")
MuldataList = select_eval_data("eva_mul_text")
PseudoLabelDataList = []
for engData in EngdataList:
    pseudo_label = emo.identifyEmotion(engData.clean_text)

    pseudoData = EvaTextData()
    pseudoData.id = engData.id
    pseudoData.pseudo_label = pseudo_label
    PseudoLabelDataList.append(pseudoData)

update_pseudo_label("eva_eng_text", PseudoLabelDataList)
update_pseudo_label("eva_mul_text", PseudoLabelDataList)
