import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector
from transformers import BertTokenizer, BertForSequenceClassification, XLMRobertaTokenizer,XLMRobertaForSequenceClassification
import torch
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
                select id, clean_text, pseudo_label from tweets where length(clean_text) > 0 limit 0, 5
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
    predicted_datalist = evaluation(textList, tokenizer, model)
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
    predicted_datalist = evaluation(data_list, tokenizer, model)
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
        update_sql = "Update tweets set " + colname + "= %s where id = %s"

        values = []

        for textData in textDataList:
            tuppleData = (textData.id, textData.predicted_label)
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

