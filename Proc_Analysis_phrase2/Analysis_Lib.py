
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

import commons.DataClass.Variable as commonlib

class EvaTextData:
    id = "",
    thetext = "",
    label = "",
    dstype = "",
    labeltype = ""
    predictedLabel = ""

    def __init__(self, id, thetext, label, dstype, labeltype):
        self.id = id
        self.thetext = thetext
        self.label = label
        self.dstype = dstype
        self.labeltype = labeltype
        self.predictedLabel = None

    def __init__(self, id, thetext, label):
        self.id = id
        self.thetext = thetext
        self.label = label

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

def get_cleanned_ori_text(tableName, colName):
    """
    Query the cleanned text info.
    :return:
    """

    print("Start to query ...")
    TextDataList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = "select id, thetext, label, dstype, labeltype from " + tableName + " where " + colName + " is null"
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

def get_cleanned_ori_tweets(tableName, colName):
    """
    Query the cleanned text info.
    :return:
    """

    print("Start to query ...")
    TextDataList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = "select id, clean_text, pseudo_label from " + tableName + " where " + colName + " is null"
        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            thetext = i[1]
            label = i[2]

            data = EvaTextData(id, thetext, label)
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

def prepare_model_mBERT():
    model_name = "bert-base-multilingual-uncased"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=commonlib.NUM_CLASSES)
    return model, tokenizer

def prepare_model_xlmr():
    model_name = "FacebookAI/xlm-roberta-base"
    tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
    model = XLMRobertaForSequenceClassification.from_pretrained(model_name, num_labels=commonlib.NUM_CLASSES)
    return model, tokenizer

def evaluation(textList, tokenizer, model):
    """
    Generate the predicted emotion for the texts.
    :param textList: The passed in texts list
    :param tokenizer: The tokenizer of the model
    :param model: The model object
    :return: The textList with predicted emotion
    """

    predicted_list = []
    for text in textList:
        try:
            # Tokenize input text
            inputs = tokenizer(text.thetext, return_tensors='pt')

            # Perform classification
            with torch.no_grad():
                outputs = model(**inputs)

            # Get predicted label (assuming binary classification)
            predicted_label = torch.argmax(outputs.logits, dim=1).item()

            text.predictedLabel = predicted_label
            predicted_list.append(text)

        except:
            text.predictedLabel = "X"
            predicted_list.append(text)
            print("Problem found at text id: " + str(text.id))

    return predicted_list

def prediction_mbert(selected_Model, modelPath, textList):
    """
    Perform predcition by mBERT
    :param selected_Model: The model object
    :param modelPath: The model file path
    :param textList: The pass in text list
    :return: The text list with predicted info
    """

    # Prepare the model, tokenizer
    print("Prepare model and tokenizer ... start")
    model, tokenizer = prepare_model_mBERT()
    print("Prepare model and tokenizer ... end")

    # Load the model
    print("Load model ... start")
    state_dict = torch.load(modelPath + selected_Model.fileName)
    model.load_state_dict(state_dict)
    print("Load model ... end")

    # 5. Set the model to evaluation mode
    model.eval()

    # 6. Predictin process
    print("Predicting process ... start")
    predicted_datalist = evaluation(textList, tokenizer, model)
    print("Predicting process ... end")
    return predicted_datalist

def prediction_xlmr(selected_Model, modelPath, data_list):
    """
    Perform predcition by FB-XLM-R
    :param selected_Model: The model object
    :param modelPath: The model file path
    :param textList: The pass in text list
    :return: The text list with predicted info
    """

    # Prepare the model, tokenizer
    print("Prepare model and tokenizer ... start")
    model, tokenizer = prepare_model_xlmr()
    print("Prepare model and tokenizer ... end")

    # Load the model
    print("Load model ... start")
    state_dict = torch.load(modelPath + selected_Model.fileName)
    model.load_state_dict(state_dict)
    print("Load model ... end")

    # 5. Set the model to evaluation mode
    model.eval()

    # 6. Predictin process
    print("Predicting process ... start")
    predicted_datalist = evaluation(data_list, tokenizer, model)
    print("Predicting process ... end")
    return predicted_datalist


def update_prediction_result(textDataList, tablename, colname):
    """
    Update the predicted result in the tweets table
    :param textDataList: The pass in text data list with predicted label
    :param colname: the column name to be updated
    :return: Nothing
    """
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        update_sql = "Update " + tablename + " set " + colname + "= %s where id = %s "

        values = []

        for textData in textDataList:
            tuppleData = (textData.predictedLabel, textData.id)
            values.append(tuppleData)

        # executemany() method
        mycursor.executemany(update_sql, values)
        # save changes
        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to insert record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")