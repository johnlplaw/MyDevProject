import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector
from transformers import BertTokenizer, BertForSequenceClassification
import torch
###################
# Model types
MODEL_MBERT_ENG = "mbert_eng"
MODEL_MBERT_MUL = "mbert_mul"
MODEL_XLMR_ENG = "xlmr_eng"
MODEL_XLMR_MUL = "xlmr_mul"

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
    print("Start to query ...")
    TextDataList = []
    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        Select_sql = """
                select id, clean_text, pseudo_label from tweets where length(clean_text) > 0 limit 0, 100
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
    predicted_list = []
    for text in textList:
        print(text.id)
        # Tokenize input text
        inputs = tokenizer(text.clean_text, return_tensors='pt')

        # Perform classification
        with torch.no_grad():
            outputs = model(**inputs)

        # Get predicted label (assuming binary classification)
        predicted_label = torch.argmax(outputs.logits, dim=1).item()
        print(predicted_label)
        text.setPredictedLabel(predicted_label)
        predicted_list.append(text)

    return predicted_list


def prepare_model_mBERT_Eng():
    model_name = "bert-base-multilingual-uncased"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=NUM_CLASSES)
    return model, tokenizer


#
# theDataList = get_cleanned_ori_text()
# for disp in theDataList:
#     print(str(disp.id) + " / " + disp.clean_text+ " / " + disp.pseudo_label )




