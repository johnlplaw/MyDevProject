import os.path as ospath
import pickle
import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector
from sklearn.model_selection import train_test_split

"""
This script is for retrieving the evaluation dataset from all the training data (2800) for each GPT and Syn dataset 
including all the label, plabel and slabel. After done the retrieving dataset, insert the dataset into EVATEXT table.
"""

dirPath = './output'
DsType_gpt = 'chatgpt'
DsType_mul = 'multiLangComb_nos'
LblType_label = "la"
LblType_plabel = "pla"
LblType_slabel = "sla"

dsTypeList = [DsType_gpt, DsType_mul]
labelTypeList = [LblType_label, LblType_plabel, LblType_slabel]

class EvaText:
    label = ""
    text = ""
    labelType=""
    dsType=""

    def __init__(self, label, text, labelType, dsType):
        self.label = label
        self.text = text
        self.labelType = labelType
        self.dsType = dsType

    def toString(self):
        print(self.label + " / " +
        self.text + " / " +
        self.labelType + " / " +
        self.dsType + " / " )


def convertLabelType(lbl):
    returnStr = ""
    if LblType_label == lbl:
        returnStr = "lbl"
    elif LblType_plabel == lbl:
        returnStr = "plbl"
    elif LblType_slabel == lbl:
        returnStr = "slbl"
    return returnStr

def loadTrainingDs(dsType, labelType):
    fileName = ""
    if dsType == DsType_gpt:
        #
        fileName = "DataFrame_"+ dsType+"_resampling_2800_"+labelType+"bel.obj"
    elif dsType == DsType_mul:
        #
        fileName = "DataFrame_training_multi_nos_"+convertLabelType(labelType)+"_2800.obj"

    return fileName



def GetDSObj(fileName):
    fileObj = open(fileName, 'rb')
    df = pickle.load(fileObj)
    fileObj.close()
    return df

def getTxtColName(dsType):
    if dsType == DsType_gpt:
        colName = "txt"
    elif dsType == DsType_mul:
        colName = "multilang_text"
    return colName

def getLabelColName(dsType, labelType):
    if dsType == DsType_gpt:
        if (labelType == LblType_label):
            labelName = "label"
        elif (labelType == LblType_plabel):
            labelName = "plabel"
        elif (labelType == LblType_slabel):
            labelName = "slabel"

    elif dsType == DsType_mul:
        labelName = "std_label"
    return labelName

def GetTextListFromDS(df, dsType, labelType):
    txtList = df[getTxtColName(dsType)].tolist()
    labelList = df[getLabelColName(dsType, labelType)].tolist()
    txtClassList = []
    for i in range(len(txtList)):
        txtclass = EvaText(labelList[i], txtList[i], labelType, dsType)
        txtClassList.append(txtclass)
    return txtClassList

def GetTxt(ds, dsType, labelType):

    filePath = dirPath + "/" + ds
    isFound = ospath.isfile(filePath)
    print(ds + " - " + str(isFound))
    df = GetDSObj(filePath)
    train_dataset, val_dataset = train_test_split(df, test_size=0.2, random_state=42)

    print(len(train_dataset))
    print(len(val_dataset))

    textList = GetTextListFromDS(val_dataset, dsType, labelType)
    return textList

def GetDSList():
    dsNameList = []
    for dstype in dsTypeList:
        for labelType in labelTypeList:
            dsName = loadTrainingDs(dstype, labelType)
            classList = GetTxt(dsName, dstype, labelType)
            print(len(classList))
            dsNameList.append(classList)
    return dsNameList

def InsertData(list):
    print("Insert into mysql - start")
    conn = sqlHelper.get_mysql_conn()
    mycursor = conn.cursor()
    sql = "INSERT INTO EvaText (thetext, label, dsType, labelType) VALUES (%s, %s, %s, %s)"

    for txtdata in list:
        val = (txtdata.text, txtdata.label, txtdata.dsType, txtdata.labelType)
        mycursor.execute(sql, val)

    conn.commit()
    print(mycursor.rowcount, "record inserted.")

    print("Insert into mysql - end")


txtList = GetDSList()

for item in txtList:
    InsertData(item)