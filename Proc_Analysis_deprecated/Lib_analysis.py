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
"""
The common library script for collecting all the shared functons.
"""

###################
# Model types
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


NUM_CLASSES = 6

EMOTION_LABEL_NEUTRAL_CODE = 0
EMOTION_LABEL_HAPPY_CODE = 1
EMOTION_LABEL_FEAR_CODE = 2
EMOTION_LABEL_SURPRISE_CODE = 3
EMOTION_LABEL_ANGRY_CODE = 4
EMOTION_LABEL_SAD_CODE = 5

EMOTION_LABEL_NEUTRAL = 'Neutral'
EMOTION_LABEL_HAPPY = 'Happy'
EMOTION_LABEL_FEAR = 'Fear'
EMOTION_LABEL_SURPRISE = 'Surprise'
EMOTION_LABEL_ANGRY = 'Angry'
EMOTION_LABEL_SAD = 'Sad'

Label_Desc_Code = {
    EMOTION_LABEL_NEUTRAL: EMOTION_LABEL_NEUTRAL_CODE,
    EMOTION_LABEL_HAPPY: EMOTION_LABEL_HAPPY_CODE,
    EMOTION_LABEL_FEAR: EMOTION_LABEL_FEAR_CODE,
    EMOTION_LABEL_SURPRISE: EMOTION_LABEL_SURPRISE_CODE,
    EMOTION_LABEL_ANGRY: EMOTION_LABEL_ANGRY_CODE,
    EMOTION_LABEL_SAD: EMOTION_LABEL_SAD_CODE
}

Label_Code_Desc = {
    EMOTION_LABEL_NEUTRAL_CODE: EMOTION_LABEL_NEUTRAL,
    EMOTION_LABEL_HAPPY_CODE: EMOTION_LABEL_HAPPY,
    EMOTION_LABEL_FEAR_CODE: EMOTION_LABEL_FEAR,
    EMOTION_LABEL_SURPRISE_CODE: EMOTION_LABEL_SURPRISE,
    EMOTION_LABEL_ANGRY_CODE: EMOTION_LABEL_ANGRY,
    EMOTION_LABEL_SAD_CODE: EMOTION_LABEL_SAD
}

LabelList = [EMOTION_LABEL_NEUTRAL, EMOTION_LABEL_HAPPY, EMOTION_LABEL_FEAR, EMOTION_LABEL_SURPRISE, EMOTION_LABEL_ANGRY, EMOTION_LABEL_SAD]
###################

class TextData:
    """
    TextData class to store the tweets info.
    """

    id = ""
    clean_text = ""
    pseudo_label = ""
    predicted_label = ""

    def __init__(self, id, clean_text, pseudo_label, predicted_label):
        self.id = id;
        self.clean_text = clean_text
        self.pseudo_label = pseudo_label
        self.predicted_label = predicted_label

    def setPredictedLabel(self, predicted_label):
        self.predicted_label = predicted_label

class TestingData:
    """
    TestingData class to store the testing info.
    """

    id = ""
    clean_text = ""
    pseudo_label = ""
    label = ""

    def __init__(self, id, clean_text, pseudo_label, label):
        self.id = id
        self.clean_text = clean_text
        self.pseudo_label = pseudo_label
        self.label = label

    def setPredictedLabel(self, predicted_label):
        self.predicted_label = predicted_label

class Lang_Model:
    """
    Language Model info.
    """

    def __init__(self, modelName, colName):
        self.modelName = modelName
        self.colName = colName

#####################

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
                select id, clean_text, pseudo_label from tweets where length(clean_text) > 0
                """
        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            clean_text = i[1]
            pseudo_label = i[2]

            data = TextData(id, clean_text, pseudo_label, "")
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

def get_cleanned_testing_text(tableStr):
    """
    Query the testing text info.
    :return:
    """

    print("Start to query ...")
    TextDataList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = "select id, clean_text, label, pseudo_label from " + tableStr + "  where length(clean_text) > 0"
        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            id = i[0]
            clean_text = i[1]
            label = i[2]
            pseudo_label = i[3]

            data = TestingData(id, clean_text, pseudo_label, label)
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

        # Tokenize input text
        inputs = tokenizer(text.clean_text, return_tensors='pt')

        # Perform classification
        with torch.no_grad():
            outputs = model(**inputs)

        # Get predicted label (assuming binary classification)
        predicted_label = torch.argmax(outputs.logits, dim=1).item()

        text.setPredictedLabel(predicted_label)
        predicted_list.append(text)

    return predicted_list


def prepare_model_mBERT():
    model_name = "bert-base-multilingual-uncased"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)
    return model, tokenizer

def prepare_model_xlmr():
    model_name = "FacebookAI/xlm-roberta-base"
    tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
    model = XLMRobertaForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)
    return model, tokenizer

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


def update_prediction_result(textDataList, colname):
    """
    Update the predicted result in the tweets table
    :param textDataList: The pass in text data list with predicted label
    :param colname: the column name to be updated
    :return: Nothing
    """
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        update_sql = "Update tweets set " + colname + "= %s where id = %s "

        values = []

        for textData in textDataList:
            tuppleData = (Label_Code_Desc[textData.predicted_label], textData.id)
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

def update_prediction_result_for_TestDS(textDataList, tablename, colname):
    """
    Update the predicted result in the given table
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
            tuppleData = (Label_Code_Desc[textData.predicted_label], textData.id)
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



def analysis_compare (model_name, y_true_multi, y_pred_multi, labelList, evaType):
    """
    If the pseudo-labelling is standard, how other models performs if compare to the pseudo-labelling.
    :param model_name: The model name
    :param y_true_multi: The pseudo-labelling list
    :param y_pred_multi: The predicted label list from the model
    :return:
    """

    outPath = "./output/"
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


def get_Label(colName):
    """
    Get label list from tweets table.
    :param colName: The column name
    :return:
    """

    print("Start to query ...")
    labelList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = "select " + colName + " from selectedtweets where not (clean_text is null or clean_text = '') order by id "
        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            pseudo_label = i[0]
            labelList.append(pseudo_label)

        print("Finish query ...")
    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return labelList

def get_Testing_Label(tableName, colName):
    """
    Get label list from tweets table.
    :param colName: The column name
    :return:
    """

    print("Start to query ...")
    labelList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = "select " + colName + " from " + tableName + " where not (clean_text is null or clean_text = '') order by id "
        mycursor.execute(Select_sql)
        result = mycursor.fetchall()

        for i in result:
            pseudo_label = i[0]
            labelList.append(pseudo_label)

        print("Finish query ...")
    except mysql.connector.Error as error:
        print("Failed to select record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")

    return labelList

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

def plotHeatMapKappaScore(data, raters, labelList):
    outPath = "./output/"
    sns.heatmap(
        data,
        mask=np.tri(len(raters)),
        annot=True, linewidths=5,
        vmin=0, vmax=1,
        xticklabels=labelList,
        yticklabels=labelList,
    )
    plt.show()
    #plt.savefig(outPath + 'KappaAgreement.png')