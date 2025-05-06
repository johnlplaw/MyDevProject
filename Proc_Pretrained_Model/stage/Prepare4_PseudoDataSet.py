import Variable as var
import pickle
import commons.mysql.mysqlHelper as sqlHelper
from translate_shell.translate import translate
import commons.emotion.identifyEmotion as emo

"""
This script is for preparing the pseudo-labeling by text2emotion library for the selected training dataset. This will
provide the datasets for comparing and study the impacts of the two labelling system.
"""

class SynDataContent:
    lang_type = ""
    ori_text = ""
    mul_text = ""
    lang_col = ""
    label = ""
    plabel = ""

def Get_DataFrame(df_type, size):
    file_name = df_type + str(size) + ".obj"
    fileObj = open(file_name, 'rb')
    df = pickle.load(fileObj)
    fileObj.close()
    return df

def insert_data(theContentList):
    conn = sqlHelper.get_mysql_conn()
    mycursor = conn.cursor()
    sql = "INSERT INTO Resample_synth_text (lang_type, ori_text, mul_text, lang_col, label, plabel) VALUES (%s, %s, %s, %s, %s, %s)"

    for content in theContentList:
        val = (content.lang_type, content.ori_text, content.mul_text, content.lang_col, content.label, content.plabel)
        mycursor.execute(sql, val)

    conn.commit()
    print(mycursor.rowcount, "record inserted.")



# Step 1: The selected datasets from the synthetic dataset
dataset_size_list = [var.SAMPLING_400, var.SAMPLING_1600, var.SAMPLING_2800]


for size in dataset_size_list:
    langType = "E"
    df = Get_DataFrame(var.FILE_TRAINING_ENG_NOS_LBL, size)
    print(str(size) + "-" + str(len(df)))
    contentList = []
    for index, row in df.iterrows():
        obj = SynDataContent()
        obj.lang_type = langType + str(size)
        obj.ori_text = row[var.COLUMN_NAME_ENG_TXT]
        obj.mul_text = None
        obj.lang_col = None
        obj.label = var.Label_Code_Desc[int(row[var.COLUMN_NAME_STD_LABEL])]
        obj.plabel = emo.identifyEmotion(obj.ori_text)
        print(obj.ori_text + " /" + obj.plabel)
        contentList.append(obj)
    insert_data(contentList)

for size in dataset_size_list:
    langType = "M"
    df = Get_DataFrame(var.FILE_TRAINING_MUL_NOS_LBL, size)
    print(str(size) + "-" + str(len(df)))
    contentList = []
    for index, row in df.iterrows():
        obj = SynDataContent()
        obj.lang_type = langType + str(size)
        obj.ori_text = row[var.COLUMN_NAME_ENG_TXT]
        obj.mul_text = row[var.COLUMN_NAME_MULTI_LANG_TXT]
        obj.lang_col = row[var.COLUMN_NAME_SRC_TYPE]
        obj.label = var.Label_Code_Desc[int(row[var.COLUMN_NAME_STD_LABEL])]
        obj.plabel = emo.identifyEmotion(obj.ori_text)
        print(obj.ori_text + " /" + obj.plabel)
        contentList.append(obj)
    insert_data(contentList)

