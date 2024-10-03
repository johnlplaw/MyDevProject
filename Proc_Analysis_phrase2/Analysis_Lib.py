
import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector
from transformers import BertTokenizer, BertForSequenceClassification, XLMRobertaTokenizer,XLMRobertaForSequenceClassification
import torch
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report, roc_curve, auc
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle
from sklearn.preprocessing import LabelEncoder
import itertools

from sklearn.metrics import cohen_kappa_score

class EvaTextData:
    id = "",
    thetext = "",
    label = "",
    dstype = "",
    labeltype = ""

    def __init__(self, id, thetext, label, dstype, labeltype):
        self.id = id
        self.thetext = thetext
        self.label = label
        self.dstype = dstype
        self.labeltype = labeltype

    def toString(self):
        print(self.id + " / " +
        self.thetext + " / " +
        self.label + " / " +
        self.dstype + " / " +
        self.labeltype )

class Selected_Model:
    """
    Model info.
    """
    def __init__(self, fileName, modelName, colName):
        self.fileName = fileName
        self.modelName = modelName
        self.colName = colName

def get_cleanned_ori_text():
    """
    Query the cleanned text info.
    :return:
    """

    print("Start to query ...")
    TextDataList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = """
            select id, thetext, label, dstype, labeltype from EvaText;
        """
        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            thetext = i[1]
            label = i[2]
            dstype = i[3]
            labeltype = i[4]

            data = EvaTextData(id, thetext, label, dstype, labeltype)
            TextDataList.append(data)

        print("Finish query ...")
    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return TextDataList



COL_GPT_LBL_XMLB = "GPT_LBL_XMLB"
COL_GPT_PLBL_XMLB = "GPT_PLBL_XMLB"
COL_GPT_SLBL_XMLB = "GPT_SLBL_XMLB"
COL_GPT_LBL_MBERT = "GPT_LBL_MBERT"
COL_GPT_PLBL_MBERT = "GPT_PLBL_MBERT"
COL_GPT_SLBL_MBERT = "GPT_SLBL_MBERT"

COL_SYN_LBL_XMLB = "SYN_LBL_XMLB"
COL_SYN_PLBL_XMLB = "SYN_PLBL_XMLB"
COL_SYN_SLBL_XMLB = "SYN_SLBL_XMLB"
COL_SYN_LBL_MBERT = "SYN_LBL_MBERT"
COL_SYN_PLBL_MBERT = "SYN_PLBL_MBERT"
COL_SYN_SLBL_MBERT = "SYN_SLBL_MBERT"

COL_SYN_LBL_XMLB_E = "SYN_LBL_XMLB_E"
COL_SYN_PLBL_XMLB_E = "SYN_PLBL_XMLB_E"
COL_SYN_SLBL_XMLB_E = "SYN_SLBL_XMLB_E"
COL_SYN_LBL_MBERT_E = "SYN_LBL_MBERT_E"
COL_SYN_PLBL_MBERT_E = "SYN_PLBL_MBERT_E"
COL_SYN_SLBL_MBERT_E = "SYN_SLBL_MBERTE"