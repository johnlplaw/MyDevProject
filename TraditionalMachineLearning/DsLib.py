import pickle

dsFolder = "../Proc_Pretrained_Model/RecordedResult"
ChatGPTdsFolder = "../Proc_Pretrained_model_ChatGPTDS/RecordedResult"

def getEngDS(size, lbltype):
    dsEngFile = "DataFrame_training_eng_nos_" + lbltype + "_" + str(size) + ".obj"
    filePath = dsFolder + "/" + dsEngFile
    fileObj = open(filePath, 'rb')
    engDF = pickle.load(fileObj)
    fileObj.close()
    return engDF

def getMulDS(size, lbltype):
    dsMulFile = "DataFrame_training_multi_nos_" + lbltype + "_" + str(size) + ".obj"
    filePath = dsFolder + "/" + dsMulFile
    fileObj = open(filePath, 'rb')
    mulDF = pickle.load(fileObj)
    fileObj.close()
    return mulDF

def getChatGPTMulDS(size, lbltype):
    dsMulFile = "DataFrame_chatgpt_resampling_" + str(size) + "_" + lbltype + ".obj"
    filePath = ChatGPTdsFolder + "/" + dsMulFile
    fileObj = open(filePath, 'rb')
    mulDF = pickle.load(fileObj)
    fileObj.close()
    return mulDF

def getDataLists(size, lbltype):

    df = getEngDS(size, lbltype)
    textList = df['cleanedtxt'].to_list()
    labelList = df['std_label'].to_list()

    return textList, labelList

def getDataMulLists(size, lbltype):
    df = getMulDS(size, lbltype)
    textList = df['multilang_text'].to_list()
    labelList = df['std_label'].to_list()

    return textList, labelList

def getChatGPTDataMulLists(size, lbltype):
    df = getChatGPTMulDS(size, lbltype)
    print(df.columns)

    textList = df['txt'].to_list()
    labelList = df[lbltype].to_list()

    return textList, labelList


# textList1, labelList1 = getDataLists()
# textList2, labelList2 = getDataMulLists()
#
# print(textList1[0:60])
# print(textList2[0:60])