
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

CleanTxt = "AND NOT (GPT_LBL_XMLB= 'X' or GPT_PLBL_XMLB= 'X' or GPT_SLBL_XMLB= 'X' or GPT_LBL_MBERT= 'X' or GPT_PLBL_MBERT= 'X' or GPT_SLBL_MBERT= 'X' or SYN_LBL_XMLB= 'X' or SYN_PLBL_XMLB= 'X' or SYN_SLBL_XMLB= 'X' or SYN_LBL_MBERT= 'X' or SYN_PLBL_MBERT= 'X' or SYN_SLBL_MBERT= 'X' or SYN_LBL_XMLB_E= 'X' or SYN_PLBL_XMLB_E= 'X' or SYN_SLBL_XMLB_E= 'X' or SYN_LBL_MBERT_E= 'X' or SYN_PLBL_MBERT_E= 'X' or SYN_SLBL_MBERTE= 'X') "

def get_Label_List(tableName, colName, dsType, labelType):
    """
    Query the cleanned text info.
    :return:
    """

    print("Start to query ...")
    LabelList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = "select " + colName + " from " + tableName + " where dstype = '" + dsType + "' and labeltype = '" + labelType + "' " + CleanTxt

        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            label = i[0]
            LabelList.append(label)
        print("Finish query ...")
    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return LabelList

def get_Label_List_tweets(tableName, colName):
    """
    Query the cleanned text info.
    :return:
    """

    print("Start to query ...")
    LabelList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = "select " + colName + " from " + tableName

        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            label = i[0]
            LabelList.append(label)
        print("Finish query ...")
    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return LabelList


def analysis_compare (model_name, y_true_multi, y_pred_multi, labelList, evaType):
    """
    If the pseudo-labelling is standard, how other models performs if compare to the pseudo-labelling.
    :param model_name: The model name
    :param y_true_multi: The pseudo-labelling list
    :param y_pred_multi: The predicted label list from the model
    :return:
    """

    outPath = "./outputPerformance/"
    # Calculate confusion matrix
    conf_matrix_multi = confusion_matrix(y_true_multi, y_pred_multi, labels=labelList)

    # Calculate evaluation metrics
    accuracy_multi = accuracy_score(y_true_multi, y_pred_multi)
    precision_micro = precision_score(y_true_multi, y_pred_multi, average='micro')
    recall_micro = recall_score(y_true_multi, y_pred_multi, average='micro')
    f1_micro = f1_score(y_true_multi, y_pred_multi, average='micro')

    precision_macro = precision_score(y_true_multi, y_pred_multi, average='macro')
    recall_macro = recall_score(y_true_multi, y_pred_multi, average='macro')
    f1_macro = f1_score(y_true_multi, y_pred_multi, average='macro')

    # Print evaluation metrics
    print("Confusion Matrix:")
    print(conf_matrix_multi)
    print("Accuracy:", accuracy_multi)
    print("Precision (Micro):", precision_micro)
    print("Recall (Micro):", recall_micro)
    print("F1-score (Micro):", f1_micro)
    print("Precision (Macro):", precision_macro)
    print("Recall (Macro):", recall_macro)
    print("F1-score (Macro):", f1_macro)

    # Classification report
    print("Classification Report:")
    print(classification_report(y_true_multi, y_pred_multi))


    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix_multi, annot=True, fmt='d', cmap='Blues', cbar=False, square=True, xticklabels=labelList, yticklabels=labelList)
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title('Confusion Matrix')
    # Save the plotted graph
    plt.savefig(outPath + model_name + '_conf_matrix' + evaType + '.png')



    # Compute ROC curve and ROC area for each class

    # Encode labels into numerical representations
    label_encoder = LabelEncoder()
    y_true_encoded = label_encoder.fit_transform(y_true_multi)
    y_pred_encoded = label_encoder.transform(y_pred_multi)

    labelList = label_encoder.classes_
    print("Label in ROC Curve:")
    print(labelList)

    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    n_classes = len(np.unique(y_true_encoded))
    print(str("--->" + str(n_classes)))
    for i in range(n_classes):
        y_true_binary = np.array([1 if label == i else 0 for label in y_true_encoded])
        y_pred_binary = np.array([1 if label == i else 0 for label in y_pred_encoded])
        fpr[i], tpr[i], _ = roc_curve(y_true_binary, y_pred_binary)
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Plot ROC curve for each class
    plt.figure(figsize=(10, 8))
    lw = 2
    colors = ['aqua', 'darkorange', 'cornflowerblue', 'brown', 'chartreuse', 'coral']
    for i, color in zip(range(n_classes), colors):

        plt.plot(fpr[i], tpr[i], color=color, lw=lw,
                 label='ROC curve of class {0} (area = {1:0.2f})'
                 ''.format(labelList[i], roc_auc[i]))

    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve for Multi-class Classification')
    plt.legend(loc="lower right")
    #plt.show()

    # Save the plotted graph
    plt.savefig(outPath + model_name + '_roc_curve' + evaType + '.png')

EMOTION_LABEL_NEUTRAL_CODE = "0"
EMOTION_LABEL_HAPPY_CODE = "1"
EMOTION_LABEL_FEAR_CODE = "2"
EMOTION_LABEL_SURPRISE_CODE = "3"
EMOTION_LABEL_ANGRY_CODE = "4"
EMOTION_LABEL_SAD_CODE = "5"

LabelList = [EMOTION_LABEL_NEUTRAL_CODE, EMOTION_LABEL_HAPPY_CODE, EMOTION_LABEL_FEAR_CODE, EMOTION_LABEL_SURPRISE_CODE, EMOTION_LABEL_ANGRY_CODE, EMOTION_LABEL_SAD_CODE]

def calculate_Cohen_Kappa_Score(raters):
    """
    Calculate the Cohen Kappa Score
    :param raters: The list of the labels representing the raters
    :return:
    """
    data = np.zeros((len(raters), len(raters)))
    # Calculate cohen_kappa_score for every combination of raters
    # Combinations are only calculated j -> k, but not k -> j, which are equal
    # So not all places in the matrix are filled.
    for j, k in list(itertools.combinations(range(len(raters)), r=2)):
        data[j, k] = cohen_kappa_score(raters[j], raters[k])

    print(data)
    return data

def plotHeatMapKappaScore(data, raters, labelList, datasetType):
    outPath = "./outputAggrement/"
    sns.heatmap(
        data,
        mask=np.tri(len(raters)),
        annot=True, linewidths=5,
        vmin=0, vmax=1,
        xticklabels=labelList,
        yticklabels=labelList,
    )
    #plt.show()
    plt.savefig(outPath + 'KappaAgreement_' + datasetType + '.png')
    plt.clf()